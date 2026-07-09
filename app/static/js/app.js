// Dark mode toggle
document.addEventListener('click', function (e) {
  const btn = e.target.closest('[data-theme-toggle]');
  if (!btn) return;
  const root = document.documentElement;
  const isDark = root.classList.toggle('dark');
  localStorage.setItem('theme', isDark ? 'dark' : 'light');
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

// Completion gate. Lessons with a quiz require passing it; lessons without
// one keep the light gate of opening at least one self-check answer.
function initCompleteGate() {
  const form = document.querySelector('#complete-zone form[data-complete-gate]');
  const button = form && form.querySelector('button');
  const hint = document.querySelector('#complete-zone [data-gate-hint]');
  if (!button || button.dataset.gateReady) return;

  const quizGate = form.dataset.gateQuiz;
  const checks = document.querySelectorAll('.prose-lesson details.selfcheck');
  if (!quizGate && !checks.length) return;
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

function initLessonExtras() {
  initMentorTips();
  initCompleteGate();
}

initLessonExtras();
document.body.addEventListener('htmx:afterSwap', function () { initLessonExtras(); });
