// Dark mode toggle
document.addEventListener('click', function (e) {
  const btn = e.target.closest('[data-theme-toggle]');
  if (!btn) return;
  const root = document.documentElement;
  const isDark = root.classList.toggle('dark');
  localStorage.setItem('theme', isDark ? 'dark' : 'light');
});

// All state-changing browser requests carry the session-bound CSRF token.
function csrfToken() {
  const meta = document.querySelector('meta[name="csrf-token"]');
  return meta ? meta.content : '';
}

document.addEventListener('submit', function (e) {
  const form = e.target;
  if (!form || String(form.method).toLowerCase() !== 'post' || !csrfToken()) return;
  if (!form.querySelector('input[name="csrf_token"]')) {
    const input = document.createElement('input');
    input.type = 'hidden';
    input.name = 'csrf_token';
    input.value = csrfToken();
    form.appendChild(input);
  }
});

document.body.addEventListener('htmx:configRequest', function (e) {
  if (csrfToken()) e.detail.headers['X-CSRF-Token'] = csrfToken();
});

// Auto-scroll AI Mentor chat to the bottom after HTMX swaps in new messages.
document.body.addEventListener('htmx:afterSwap', function (e) {
  const log = document.getElementById('chat-log');
  if (log) log.scrollTop = log.scrollHeight;
});

// Learning-path picker: a segmented toggle that shows one path's courses at a
// time. The choice is remembered across pages (catalog + dashboard).
const PATH_KEY = 'learning_path';
const PATH_TAB_ON = ['bg-white', 'dark:bg-stone-800', 'shadow-sm', 'text-stone-900', 'dark:text-white'];
const PATH_TAB_OFF = ['text-stone-500', 'hover:text-stone-900', 'dark:hover:text-white'];

function initPathPickers(root) {
  (root || document).querySelectorAll('[data-path-picker]').forEach(function (picker) {
    if (picker.dataset.pickerReady) return;
    picker.dataset.pickerReady = '1';

    const tabs = Array.from(picker.querySelectorAll('[data-path-tab]'));
    const panels = Array.from(picker.querySelectorAll('[data-path-panel]'));
    if (!tabs.length) return;
    const ids = tabs.map(function (t) { return t.dataset.pathTab; });

    function show(id) {
      if (ids.indexOf(id) === -1) id = ids[0];
      tabs.forEach(function (t) {
        const on = t.dataset.pathTab === id;
        PATH_TAB_ON.forEach(function (c) { t.classList.toggle(c, on); });
        PATH_TAB_OFF.forEach(function (c) { t.classList.toggle(c, !on); });
        t.setAttribute('aria-selected', on ? 'true' : 'false');
      });
      panels.forEach(function (p) { p.hidden = p.dataset.pathPanel !== id; });
      try { localStorage.setItem(PATH_KEY, id); } catch (e) {}
    }

    tabs.forEach(function (t) {
      t.addEventListener('click', function () { show(t.dataset.pathTab); });
    });

    let saved = null;
    try { saved = localStorage.getItem(PATH_KEY); } catch (e) {}
    show(ids.indexOf(saved) !== -1 ? saved : ids[0]);
  });
}

initPathPickers();
document.body.addEventListener('htmx:afterSwap', function () { initPathPickers(); });

// Landing-page decision quiz. This is deliberately local and deterministic:
// it demonstrates judgment without pretending to make a live AI request.
function initDecisionQuiz() {
  document.querySelectorAll('[data-decision-quiz]').forEach(function (quiz) {
    if (quiz.dataset.ready) return;
    quiz.dataset.ready = '1';
    const scenarios = Array.from(quiz.querySelectorAll('[data-quiz-scenario]'));
    const result = quiz.querySelector('[data-quiz-result]');
    const scoreNode = quiz.querySelector('[data-quiz-score]');
    const resultCopy = quiz.querySelector('[data-quiz-result-copy]');
    let current = 0;
    let score = 0;

    function showScenario(index) {
      scenarios.forEach(function (scenario, i) { scenario.hidden = i !== index; });
      const active = scenarios[index];
      if (!active) return;
      const progress = active.querySelector('[data-quiz-progress]');
      if (progress) progress.textContent = quiz.dataset.progressLabel + ' ' + (index + 1) + ' / ' + scenarios.length;
      active.querySelectorAll('[aria-hidden="true"] i').forEach(function (dot, i) {
        dot.classList.toggle('bg-accent-500', i <= index);
        dot.classList.toggle('bg-stone-200', i > index);
        dot.classList.toggle('dark:bg-stone-700', i > index);
      });
    }

    scenarios.forEach(function (scenario, index) {
      const answers = Array.from(scenario.querySelectorAll('[data-quiz-answer]'));
      const feedback = scenario.querySelector('[data-quiz-feedback]');
      const next = scenario.querySelector('[data-quiz-next]');
      answers.forEach(function (answer) {
        answer.addEventListener('click', function () {
          const correct = answer.dataset.quizAnswer === scenario.dataset.correct;
          if (correct) score += 1;
          answers.forEach(function (item) {
            item.disabled = true;
            item.classList.toggle('is-correct', item.dataset.quizAnswer === scenario.dataset.correct);
            item.classList.toggle('is-wrong', item === answer && !correct);
          });
          feedback.hidden = false;
          feedback.textContent = scenario.dataset.feedback;
          feedback.classList.add(correct ? 'border-green-500/40' : 'border-accent-500/40');
          feedback.classList.add(correct ? 'bg-green-500/10' : 'bg-accent-500/10');
          next.hidden = false;
          next.classList.add('inline-flex');
          next.textContent = index === scenarios.length - 1 ? quiz.dataset.resultLabel + ' →' : quiz.dataset.nextLabel + ' →';
        });
      });
      next.addEventListener('click', function () {
        if (index < scenarios.length - 1) {
          current = index + 1;
          showScenario(current);
        } else {
          scenarios.forEach(function (item) { item.hidden = true; });
          result.hidden = false;
          scoreNode.textContent = score;
          resultCopy.textContent = score >= 2 ? quiz.dataset.resultGood : quiz.dataset.resultLearn;
        }
      });
    });

    const restart = quiz.querySelector('[data-quiz-restart]');
    if (restart) restart.addEventListener('click', function () {
      current = 0;
      score = 0;
      result.hidden = true;
      scenarios.forEach(function (scenario) {
        scenario.querySelectorAll('[data-quiz-answer]').forEach(function (answer) {
          answer.disabled = false;
          answer.classList.remove('is-correct', 'is-wrong');
        });
        const feedback = scenario.querySelector('[data-quiz-feedback]');
        feedback.hidden = true;
        feedback.className = 'mt-5 rounded-xl border px-4 py-3 text-sm leading-relaxed';
        const next = scenario.querySelector('[data-quiz-next]');
        next.hidden = true;
        next.classList.remove('inline-flex');
      });
      showScenario(0);
    });

    showScenario(0);
  });
}

function initWorkflowLabs() {
  document.querySelectorAll('[data-workflow-lab]').forEach(function (lab) {
    if (lab.dataset.ready) return;
    lab.dataset.ready = '1';
    const tabs = Array.from(lab.querySelectorAll('[data-workflow-tab]'));
    const panels = Array.from(lab.querySelectorAll('[data-workflow-panel]'));
    tabs.forEach(function (tab) {
      tab.addEventListener('click', function () {
        const id = tab.dataset.workflowTab;
        tabs.forEach(function (item) {
          const active = item === tab;
          item.classList.toggle('is-active', active);
          item.setAttribute('aria-selected', active ? 'true' : 'false');
        });
        panels.forEach(function (panel) { panel.hidden = panel.dataset.workflowPanel !== id; });
      });
    });
  });
}

function initLandingInteractions() {
  initDecisionQuiz();
  initWorkflowLabs();
}

if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', initLandingInteractions, { once: true });
} else {
  initLandingInteractions();
}
document.body.addEventListener('htmx:afterSwap', initLandingInteractions);

// ---------------------------------------------------------------------------
// Lesson extras: mentor-tip buttons + self-check gating of "complete".
// ---------------------------------------------------------------------------

const LESSON_I18N = {
  lt: {
    ask: 'Klausk mentoriaus',
    check: 'Patikrink su mentoriumi',
    gateHint: 'Pirmiausia atsiverk bent vieną „Pasitikrink“ klausimą žemiau.',
    gateHintQuiz: 'Pirmiausia išspręsk žinių patikrą.',
  },
  en: {
    ask: 'Ask the mentor',
    check: 'Check with the mentor',
    gateHint: 'Open at least one self-check question above first.',
    gateHintQuiz: 'Finish the knowledge check first.',
  },
};

function lessonStrings() {
  const lang = (document.documentElement.lang || 'lt').slice(0, 2);
  return LESSON_I18N[lang] || LESSON_I18N.lt;
}

// Mentor tips are authored as blockquotes starting with a marker phrase and a
// suggested question in quotes. Add a button that drops the question into the
// mentor chat box so "ask the mentor" is one click, not copy-paste.
function initMentorTips() {
  const input = document.querySelector('#chat-log') &&
    document.querySelector('form[hx-post^="/mentor/"] textarea[name="message"]');
  document.querySelectorAll('.prose-lesson blockquote').forEach(function (quote) {
    if (quote.dataset.tipReady) return;
    const text = quote.textContent || '';
    if (!/Mentoriaus patarimas|Mentor tip|Užduoties patikra|Task check/i.test(text)) return;
    quote.dataset.tipReady = '1';
    quote.classList.add('mentor-tip');

    const match = text.match(/[„“"]([^“”"]+)[“”"]/);
    if (!match || !input) return;
    const question = match[1].trim();
    const isTaskCheck = /Užduoties patikra|Task check/i.test(text);

    const btn = document.createElement('button');
    btn.type = 'button';
    btn.className = 'mentor-tip-btn';
    btn.textContent = isTaskCheck ? lessonStrings().check : lessonStrings().ask;
    btn.addEventListener('click', function () {
      input.value = question;
      input.focus();
      input.scrollIntoView({ behavior: 'smooth', block: 'center' });
    });
    quote.appendChild(btn);
  });
}

// Completion gate. A lesson requires its quiz, interactive lab, or at least
// one self-check interaction before it can be marked complete.
function initCompleteGate() {
  const form = document.querySelector('#complete-zone form[data-complete-gate]');
  const button = form && form.querySelector('button');
  const hint = document.querySelector('#complete-zone [data-gate-hint]');
  if (!button || button.dataset.gateReady) return;

  const quizGate = form.dataset.gateQuiz;
  const checks = document.querySelectorAll('.prose-lesson details.selfcheck');
  const activityLab = document.querySelector('[data-lesson-activities]');
  if (!quizGate && !checks.length && !activityLab) return;
  button.dataset.gateReady = '1';

  function unlock() {
    button.disabled = false;
    button.classList.remove('opacity-50', 'cursor-not-allowed');
    button.removeAttribute('title');
    if (hint) hint.classList.add('hidden');
  }

  function lock() {
    button.disabled = true;
    button.classList.add('opacity-50', 'cursor-not-allowed');
    button.title = quizGate ? lessonStrings().gateHintQuiz : lessonStrings().gateHint;
    if (hint) hint.classList.remove('hidden');
  }

  if (quizGate) {
    // Server already knows a pass ("done"), or the quiz was passed earlier
    // in this page's lifetime (quiz.js sets data-quiz-passed after reporting).
    const quizRoot = document.querySelector('[data-quiz]');
    if (quizGate === 'done' || (quizRoot && quizRoot.dataset.quizPassed === '1')) return;
    lock();
    document.addEventListener('quiz:passed', unlock, { once: true });
    return;
  }

  if (activityLab) {
    lock();
    document.addEventListener('activities:completed', unlock, { once: true });
    return;
  }

  const key = 'selfcheck:' + location.pathname;
  let done = false;
  try { done = localStorage.getItem(key) === '1'; } catch (e) {}
  if (done) return;

  function unlockAndRemember() {
    try { localStorage.setItem(key, '1'); } catch (e) {}
    unlock();
  }

  lock();
  checks.forEach(function (d) {
    d.addEventListener('toggle', function () { if (d.open) unlockAndRemember(); });
  });
  // Messaging the mentor also counts as engaging with the lesson.
  document.body.addEventListener('htmx:afterRequest', function (e) {
    const el = e.detail && e.detail.elt;
    if (el && el.matches && el.matches('form[hx-post^="/mentor/"]')) unlockAndRemember();
  });
}

function initLessonExperience() {
  const layout = document.querySelector('[data-lesson-layout]');
  if (!layout) return;

  const workspaceTabs = Array.from(layout.querySelectorAll('.lesson-workspace-tabs a'));
  if (workspaceTabs.length && !layout.dataset.workspaceTabsReady) {
    layout.dataset.workspaceTabsReady = '1';
    function activate(tab) {
      workspaceTabs.forEach(function (item) {
        const active = item === tab;
        item.classList.toggle('is-active', active);
        if (active) item.setAttribute('aria-current', 'location');
        else item.removeAttribute('aria-current');
      });
    }
    workspaceTabs.forEach(function (tab) {
      tab.addEventListener('click', function () { activate(tab); });
    });
    if ('IntersectionObserver' in window) {
      const targets = workspaceTabs.map(function (tab) {
        return { tab: tab, node: document.querySelector(tab.getAttribute('href')) };
      }).filter(function (item) { return item.node; });
      const observer = new IntersectionObserver(function (entries) {
        const visible = entries.filter(function (entry) { return entry.isIntersecting; })
          .sort(function (a, b) { return b.intersectionRatio - a.intersectionRatio; });
        if (!visible.length) return;
        const match = targets.find(function (item) { return item.node === visible[0].target; });
        if (match) activate(match.tab);
      }, { rootMargin: '-25% 0px -60% 0px', threshold: [0, 0.15, 0.5] });
      targets.forEach(function (item) { observer.observe(item.node); });
    }
  }

  const progress = document.querySelector('[data-reading-progress]');
  if (progress && !progress.dataset.ready) {
    progress.dataset.ready = '1';
    const updateProgress = function () {
      const max = Math.max(1, document.documentElement.scrollHeight - window.innerHeight);
      const percent = Math.min(100, Math.max(0, (window.scrollY / max) * 100));
      progress.style.width = percent + '%';
    };
    window.addEventListener('scroll', updateProgress, { passive: true });
    window.addEventListener('resize', updateProgress);
    updateProgress();
  }

  const focus = layout.querySelector('[data-focus-toggle]');
  if (focus && !focus.dataset.ready) {
    focus.dataset.ready = '1';
    focus.addEventListener('click', function () {
      const active = layout.classList.toggle('is-focus');
      const label = focus.querySelector('[data-focus-label]');
      if (label) label.textContent = active ? focus.dataset.labelOff : focus.dataset.labelOn;
      focus.setAttribute('aria-pressed', active ? 'true' : 'false');
    });
  }

  layout.querySelectorAll('.prose-lesson pre').forEach(function (block) {
    if (block.dataset.copyReady) return;
    block.dataset.copyReady = '1';
    const code = block.textContent;
    const button = document.createElement('button');
    button.type = 'button';
    button.className = 'code-copy-button';
    button.textContent = layout.dataset.copyLabel;
    button.addEventListener('click', async function () {
      try {
        await navigator.clipboard.writeText(code);
        button.textContent = layout.dataset.copiedLabel;
        setTimeout(function () { button.textContent = layout.dataset.copyLabel; }, 1400);
      } catch (e) {
        const selection = window.getSelection();
        const range = document.createRange();
        range.selectNodeContents(block);
        selection.removeAllRanges();
        selection.addRange(range);
      }
    });
    block.prepend(button);
  });

  const reflection = layout.querySelector('[data-lesson-reflection]');
  if (reflection && !reflection.dataset.ready) {
    reflection.dataset.ready = '1';
    const key = 'reflection:' + location.pathname;
    const choices = Array.from(reflection.querySelectorAll('[data-reflection-choice]'));
    const reply = reflection.querySelector('[data-reflection-reply]');
    function choose(choice) {
      choices.forEach(function (item) { item.classList.toggle('is-selected', item.dataset.reflectionChoice === choice.dataset.reflectionChoice); });
      reply.textContent = choice.dataset.reply;
      reply.hidden = false;
      try { localStorage.setItem(key, choice.dataset.reflectionChoice); } catch (e) {}
    }
    choices.forEach(function (choice) { choice.addEventListener('click', function () { choose(choice); }); });
    let saved = null;
    try { saved = localStorage.getItem(key); } catch (e) {}
    const savedChoice = choices.find(function (item) { return item.dataset.reflectionChoice === saved; });
    if (savedChoice) choose(savedChoice);
  }
}

// Interactive lesson labs are authored as JSON and rendered client-side. The
// learner's draft stays in localStorage: no private exercise text is sent to
// the server or AI mentor unless the learner explicitly copies it there.
function initLessonActivities() {
  document.querySelectorAll('[data-lesson-activities]').forEach(function (root) {
    if (root.dataset.ready) return;
    root.dataset.ready = '1';

    const payloadNode = root.querySelector('[data-activities-payload]');
    const mount = root.querySelector('[data-activities-mount]');
    if (!payloadNode || !mount) return;

    let payload;
    try { payload = JSON.parse(payloadNode.textContent); } catch (e) { return; }

    const storageKey = 'lesson-activities:' + location.pathname + ':v' + (payload.version || 1);
    let state = { answers: {}, completed: {} };
    try {
      const saved = JSON.parse(localStorage.getItem(storageKey) || 'null');
      if (saved && saved.answers && saved.completed) state = saved;
    } catch (e) {}

    const score = root.querySelector('[data-activity-score]');
    const summaryText = root.querySelector('[data-activity-summary-text]');
    const exportButton = root.querySelector('[data-activity-export]');

    function element(tag, className, text) {
      const node = document.createElement(tag);
      if (className) node.className = className;
      if (text !== undefined) node.textContent = text;
      return node;
    }

    function save() {
      try { localStorage.setItem(storageKey, JSON.stringify(state)); } catch (e) {}
      updateSummary();
    }

    function updateSummary() {
      const done = Object.values(state.completed).filter(Boolean).length;
      if (score) score.textContent = done;
      if (summaryText) {
        summaryText.textContent = done === payload.activities.length
          ? 'Puiku – atlikai visas laboratorijos veiklas. Gali eksportuoti savo darbo rezultatą.'
          : 'Atlikta ' + done + ' iš ' + payload.activities.length + ' veiklų. Tęsk – įrašai šiame įrenginyje išsaugomi automatiškai.';
      }
      if (exportButton) exportButton.disabled = done === 0;
      if (done === payload.activities.length && root.dataset.completeAnnounced !== '1') {
        root.dataset.completeAnnounced = '1';
        document.dispatchEvent(new CustomEvent('activities:completed'));
      }
    }

    function card(activity) {
      const article = element('article', 'lesson-activity-card');
      article.dataset.activityId = activity.id;
      const heading = element('div', 'lesson-activity-heading');
      const copy = element('div');
      copy.appendChild(element('h3', '', activity.title));
      copy.appendChild(element('p', '', activity.instructions));
      heading.appendChild(copy);
      const badge = element('span', 'lesson-activity-status', state.completed[activity.id] ? 'Atlikta ✓' : 'Neatlikta');
      badge.dataset.activityStatus = activity.id;
      heading.appendChild(badge);
      article.appendChild(heading);
      return article;
    }

    function mark(activity, complete) {
      state.completed[activity.id] = complete;
      const badge = root.querySelector('[data-activity-status="' + activity.id + '"]');
      if (badge) {
        badge.textContent = complete ? 'Atlikta ✓' : 'Neatlikta';
        badge.classList.toggle('is-complete', complete);
      }
      save();
    }

    function renderPromptBuilder(activity) {
      const article = card(activity);
      const layout = element('div', 'prompt-builder-grid');
      const fields = element('div', 'prompt-builder-fields');
      const preview = element('div', 'prompt-builder-preview');
      preview.appendChild(element('p', 'prompt-preview-label', 'Tavo užklausa'));
      const output = element('pre', 'prompt-preview-output');
      output.tabIndex = 0;
      preview.appendChild(output);
      const actions = element('div', 'prompt-builder-actions');
      const copyButton = element('button', 'activity-button activity-button-primary', 'Kopijuoti užklausą');
      copyButton.type = 'button';
      const resetButton = element('button', 'activity-button', 'Išvalyti');
      resetButton.type = 'button';
      actions.append(copyButton, resetButton);
      preview.appendChild(actions);

      const values = state.answers[activity.id] || {};
      const inputs = [];

      function update() {
        const parts = [];
        let filled = 0;
        activity.fields.forEach(function (field, index) {
          const value = inputs[index].value.trim();
          values[field.id] = value;
          if (value) {
            filled += 1;
            parts.push(field.prefix + ': ' + value);
          }
        });
        state.answers[activity.id] = values;
        output.textContent = parts.length ? parts.join('\n\n') : 'Pildant laukus čia atsiras vientisa užklausa.';
        mark(activity, filled >= (activity.minimum || activity.fields.length));
      }

      activity.fields.forEach(function (field) {
        const group = element('label', 'activity-field');
        group.appendChild(element('span', '', field.label));
        const textarea = document.createElement('textarea');
        textarea.rows = 3;
        textarea.placeholder = field.placeholder || '';
        textarea.value = values[field.id] || '';
        textarea.addEventListener('input', update);
        group.appendChild(textarea);
        fields.appendChild(group);
        inputs.push(textarea);
      });

      copyButton.addEventListener('click', async function () {
        if (!output.textContent || !Object.values(values).some(Boolean)) return;
        try {
          await navigator.clipboard.writeText(output.textContent);
          copyButton.textContent = 'Nukopijuota ✓';
          setTimeout(function () { copyButton.textContent = 'Kopijuoti užklausą'; }, 1400);
        } catch (e) { output.focus(); }
      });
      resetButton.addEventListener('click', function () {
        inputs.forEach(function (input) { input.value = ''; });
        activity.fields.forEach(function (field) { values[field.id] = ''; });
        update();
        inputs[0].focus();
      });

      layout.append(fields, preview);
      article.appendChild(layout);
      update();
      return article;
    }

    function renderClassify(activity) {
      const article = card(activity);
      const list = element('div', 'classify-list');
      const values = state.answers[activity.id] || {};
      const rows = [];

      activity.items.forEach(function (item, index) {
        const row = element('div', 'classify-row');
        row.appendChild(element('p', '', item.text));
        const select = document.createElement('select');
        select.setAttribute('aria-label', 'Pasirink fragmento paskirtį');
        const empty = element('option', '', 'Pasirink…');
        empty.value = '';
        select.appendChild(empty);
        activity.categories.forEach(function (category) {
          const option = element('option', '', category.label);
          option.value = category.id;
          select.appendChild(option);
        });
        select.value = values[index] || '';
        select.addEventListener('change', function () {
          values[index] = select.value;
          state.answers[activity.id] = values;
          row.classList.remove('is-correct', 'is-wrong');
          save();
        });
        row.appendChild(select);
        list.appendChild(row);
        rows.push({ row: row, select: select, answer: item.answer });
      });

      const controls = element('div', 'activity-check-row');
      const check = element('button', 'activity-button activity-button-primary', 'Patikrinti');
      check.type = 'button';
      const feedback = element('p', 'activity-feedback');
      feedback.setAttribute('aria-live', 'polite');
      check.addEventListener('click', function () {
        const allAnswered = rows.every(function (item) { return item.select.value; });
        if (!allAnswered) {
          feedback.textContent = 'Pirma pasirink atsakymą prie kiekvieno fragmento.';
          return;
        }
        let correct = 0;
        rows.forEach(function (item) {
          const right = item.select.value === item.answer;
          item.row.classList.toggle('is-correct', right);
          item.row.classList.toggle('is-wrong', !right);
          if (right) correct += 1;
        });
        const complete = correct === rows.length;
        feedback.textContent = complete ? 'Visos dalys atpažintos teisingai.' : 'Teisingai: ' + correct + ' iš ' + rows.length + '. Pataisyk raudonai pažymėtas eilutes.';
        mark(activity, complete);
      });
      controls.append(check, feedback);
      article.append(list, controls);
      return article;
    }

    function renderDiagnose(activity) {
      const article = card(activity);
      const sample = element('blockquote', 'diagnose-sample', activity.sample);
      const options = element('div', 'diagnose-options');
      const saved = new Set(state.answers[activity.id] || []);
      const inputs = [];

      activity.options.forEach(function (option) {
        const label = element('label', 'diagnose-option');
        const input = document.createElement('input');
        input.type = 'checkbox';
        input.value = option.id;
        input.checked = saved.has(option.id);
        input.addEventListener('change', function () {
          if (input.checked) saved.add(option.id); else saved.delete(option.id);
          state.answers[activity.id] = Array.from(saved);
          label.classList.remove('is-correct', 'is-wrong');
          save();
        });
        label.append(input, element('span', '', option.label));
        options.appendChild(label);
        inputs.push({ input: input, label: label, id: option.id });
      });

      const controls = element('div', 'activity-check-row');
      const check = element('button', 'activity-button activity-button-primary', 'Patikrinti diagnozę');
      check.type = 'button';
      const feedback = element('p', 'activity-feedback');
      feedback.setAttribute('aria-live', 'polite');
      check.addEventListener('click', function () {
        const answers = new Set(activity.answers);
        let complete = saved.size === answers.size;
        inputs.forEach(function (item) {
          const shouldSelect = answers.has(item.id);
          const right = item.input.checked === shouldSelect;
          complete = complete && right;
          item.label.classList.toggle('is-correct', right && item.input.checked);
          item.label.classList.toggle('is-wrong', !right);
        });
        feedback.textContent = complete ? 'Diagnozė tiksli. ' + activity.explanation : 'Dar ne viskas. Peržiūrėk pažymėtas problemas ir bandyk dar kartą.';
        mark(activity, complete);
      });
      controls.append(check, feedback);
      article.append(sample, options, controls);
      return article;
    }

    function renderDecision(activity) {
      const article = card(activity);
      if (activity.skill || activity.minutes) {
        const meta = element('div', 'mission-activity-meta');
        if (activity.skill) meta.appendChild(element('span', '', activity.skill));
        if (activity.minutes) meta.appendChild(element('span', '', activity.minutes + ' min.'));
        article.appendChild(meta);
      }
      if (activity.scenario) {
        const scenario = element('div', 'decision-scenario');
        scenario.appendChild(element('span', '', 'Situacija'));
        scenario.appendChild(element('p', '', activity.scenario));
        article.appendChild(scenario);
      }

      const choices = element('div', 'decision-choice-list');
      const feedback = element('div', 'decision-workbench-feedback');
      feedback.setAttribute('aria-live', 'polite');
      const saved = state.answers[activity.id];

      activity.choices.forEach(function (choice) {
        const button = element('button', 'decision-workbench-choice', choice.label);
        button.type = 'button';
        button.dataset.choiceId = choice.id;

        function selectChoice() {
          state.answers[activity.id] = choice.id;
          choices.querySelectorAll('button').forEach(function (item) {
            const selected = item.dataset.choiceId === choice.id;
            item.classList.toggle('is-selected', selected);
            item.classList.remove('is-correct', 'is-wrong');
            if (selected) item.classList.add(choice.correct ? 'is-correct' : 'is-wrong');
          });
          feedback.className = 'decision-workbench-feedback ' + (choice.correct ? 'is-correct' : 'is-wrong');
          feedback.textContent = choice.feedback + (choice.correct && activity.explanation ? ' ' + activity.explanation : '');
          mark(activity, Boolean(choice.correct));
        }

        button.addEventListener('click', selectChoice);
        choices.appendChild(button);
        if (saved === choice.id) setTimeout(selectChoice, 0);
      });

      article.append(choices, feedback);
      return article;
    }

    function renderArtifactBuilder(activity) {
      const article = card(activity);
      const layout = element('div', 'artifact-builder-grid');
      const fields = element('div', 'artifact-builder-fields');
      const preview = element('div', 'artifact-builder-preview');
      preview.appendChild(element('p', 'prompt-preview-label', activity.artifact_label || 'Tavo rezultatas'));
      const output = element('pre', 'artifact-preview-output');
      output.tabIndex = 0;
      preview.appendChild(output);
      const progress = element('p', 'artifact-progress');
      progress.setAttribute('aria-live', 'polite');
      preview.appendChild(progress);

      const values = state.answers[activity.id] || {};
      const inputs = [];
      function update() {
        const sections = [];
        let ready = 0;
        activity.fields.forEach(function (field, index) {
          const value = inputs[index].value.trim();
          values[field.id] = value;
          if (value.length >= (field.min_length || 1)) ready += 1;
          if (value) sections.push((field.prefix || field.label).toUpperCase() + '\n' + value);
        });
        state.answers[activity.id] = values;
        output.textContent = sections.length ? sections.join('\n\n') : 'Pildant laukus čia formuosis tavo darbo rezultatas.';
        progress.textContent = ready === activity.fields.length
          ? 'Paruošta ✓ Rezultatas išsaugotas šiame įrenginyje.'
          : 'Paruošta ' + ready + ' iš ' + activity.fields.length + ' dalių.';
        progress.classList.toggle('is-complete', ready === activity.fields.length);
        mark(activity, ready === activity.fields.length);
      }

      activity.fields.forEach(function (field) {
        const group = element('label', 'artifact-field');
        const labelRow = element('span', 'artifact-field-label');
        labelRow.appendChild(element('strong', '', field.label));
        if (field.min_length) labelRow.appendChild(element('small', '', 'bent ' + field.min_length + ' simb.'));
        group.appendChild(labelRow);
        const textarea = document.createElement('textarea');
        textarea.rows = field.rows || 3;
        textarea.placeholder = field.placeholder || '';
        textarea.value = values[field.id] || '';
        textarea.addEventListener('input', update);
        group.appendChild(textarea);
        fields.appendChild(group);
        inputs.push(textarea);
      });

      layout.append(fields, preview);
      article.appendChild(layout);
      update();
      return article;
    }

    payload.activities.forEach(function (activity) {
      let node = null;
      if (activity.type === 'prompt_builder') node = renderPromptBuilder(activity);
      if (activity.type === 'classify') node = renderClassify(activity);
      if (activity.type === 'diagnose') node = renderDiagnose(activity);
      if (activity.type === 'decision') node = renderDecision(activity);
      if (activity.type === 'artifact_builder') node = renderArtifactBuilder(activity);
      if (node) mount.appendChild(node);
    });

    if (exportButton) exportButton.addEventListener('click', function () {
      const lines = [payload.title, 'Eksportuota: ' + new Date().toLocaleString(), ''];
      payload.activities.forEach(function (activity) {
        lines.push(activity.title);
        const answer = state.answers[activity.id];
        if (activity.type === 'prompt_builder' || activity.type === 'artifact_builder') {
          activity.fields.forEach(function (field) {
            if (answer && answer[field.id]) lines.push((field.prefix || field.label) + ': ' + answer[field.id]);
          });
        } else if (activity.type === 'decision') {
          const choice = activity.choices.find(function (item) { return item.id === answer; });
          if (choice) lines.push('Pasirinkimas: ' + choice.label);
        } else {
          lines.push('Būsena: ' + (state.completed[activity.id] ? 'atlikta' : 'neatlikta'));
        }
        lines.push('');
      });
      const blob = new Blob([lines.join('\n')], { type: 'text/plain;charset=utf-8' });
      const link = document.createElement('a');
      link.href = URL.createObjectURL(blob);
      link.download = 'mano-misijos-rezultatas.txt';
      link.click();
      setTimeout(function () { URL.revokeObjectURL(link.href); }, 1000);
    });

    root.querySelectorAll('[data-activity-status]').forEach(function (badge) {
      badge.classList.toggle('is-complete', badge.textContent.indexOf('✓') !== -1);
    });
    updateSummary();
  });
}

function initLessonExtras() {
  initMentorTips();
  initCompleteGate();
  initLessonExperience();
  initLessonActivities();
}

initLessonExtras();
document.body.addEventListener('htmx:afterSwap', function () { initLessonExtras(); });
