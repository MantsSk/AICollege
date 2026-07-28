// SoloLearn-style lesson quizzes: one question at a time, instant feedback,
// mixed question types, score screen with retry. Reads its data from the
// [data-quiz-payload] JSON block rendered by partials/quiz.html.
(function () {
  'use strict';

  function el(tag, className, text) {
    const node = document.createElement(tag);
    if (className) node.className = className;
    if (text !== undefined) node.textContent = text;
    return node;
  }

  function shuffled(list) {
    const copy = list.slice();
    for (let i = copy.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      const tmp = copy[i];
      copy[i] = copy[j];
      copy[j] = tmp;
    }
    return copy;
  }

  const BTN_PRIMARY = 'px-5 py-2.5 rounded-lg bg-brand-600 text-white font-semibold hover:bg-brand-500 disabled:opacity-50 disabled:cursor-not-allowed';
  const BTN_SECONDARY = 'px-5 py-2.5 rounded-lg border border-stone-300 dark:border-stone-700 font-semibold hover:bg-stone-100 dark:hover:bg-stone-800';

  function Quiz(root, payload) {
    this.root = root;
    this.mount = root.querySelector('[data-quiz-mount]');
    this.questions = payload.quiz.questions;
    this.passPercent = payload.quiz.pass_percent || 0;
    this.strings = payload.strings;
    this.resultUrl = root.dataset.resultUrl || null;
    this.practice = root.dataset.practice === '1';
    this.reset();
  }

  Quiz.prototype.reset = function () {
    this.index = 0;
    this.score = 0;
  };

  Quiz.prototype.clear = function () {
    this.mount.textContent = '';
  };

  // ---- intro ---------------------------------------------------------------

  Quiz.prototype.renderIntro = function () {
    this.clear();
    const wrap = el('div', 'text-center py-4');
    wrap.appendChild(el('p', 'text-stone-600 dark:text-stone-400', this.strings.intro));
    const start = el('button', 'mt-5 ' + BTN_PRIMARY, this.strings.start);
    start.type = 'button';
    start.addEventListener('click', this.renderQuestion.bind(this));
    wrap.appendChild(start);
    this.mount.appendChild(wrap);
  };

  // ---- question screens ----------------------------------------------------

  Quiz.prototype.renderProgress = function () {
    const bar = el('div', 'flex items-center gap-1.5 mb-5');
    for (let i = 0; i < this.questions.length; i++) {
      const dot = el('div', 'h-1.5 flex-1 rounded-full ' +
        (i < this.index ? 'bg-brand-500' :
          i === this.index ? 'bg-brand-300 dark:bg-brand-700' :
            'bg-stone-200 dark:bg-stone-800'));
      bar.appendChild(dot);
    }
    const label = el('span', 'ml-2 shrink-0 text-xs font-medium text-stone-400 tabular-nums',
      (this.index + 1) + '/' + this.questions.length);
    bar.appendChild(label);
    return bar;
  };

  Quiz.prototype.renderQuestion = function () {
    this.clear();
    const q = this.questions[this.index];
    const wrap = el('div');
    wrap.appendChild(this.renderProgress());
    wrap.appendChild(el('p', 'font-semibold', q.prompt));

    const hintKey = { multi: 'select_all', fill: 'type_hint', gap: 'gap_hint', order: 'order_hint' }[q.type];
    if (hintKey) wrap.appendChild(el('p', 'mt-1 text-sm text-stone-500', this.strings[hintKey]));

    const body = el('div', 'mt-4');
    wrap.appendChild(body);

    const footer = el('div', 'mt-5');
    const feedback = el('div', 'hidden mb-4 rounded-lg px-4 py-3 text-sm');
    const check = el('button', BTN_PRIMARY, this.strings.check);
    check.type = 'button';
    check.disabled = true;
    footer.appendChild(feedback);
    footer.appendChild(check);
    wrap.appendChild(footer);

    // Each renderer wires up the body and returns a grade() -> bool.
    const renderer = {
      single: this.buildChoice,
      truefalse: this.buildChoice,
      multi: this.buildChoice,
      fill: this.buildFill,
      gap: this.buildGap,
      order: this.buildOrder,
    }[q.type];
    const grade = renderer.call(this, q, body, function () { check.disabled = false; }, check);

    const self = this;
    check.addEventListener('click', function () {
      if (check.dataset.next) {
        self.index += 1;
        if (self.index < self.questions.length) self.renderQuestion();
        else self.renderResult();
        return;
      }
      const result = grade();
      if (result.correct) self.score += 1;
      body.querySelectorAll('button, input').forEach(function (n) { n.disabled = true; });
      feedback.classList.remove('hidden');
      if (result.correct) {
        feedback.className = 'mb-4 rounded-lg px-4 py-3 text-sm bg-green-500/10 text-green-700 dark:text-green-400';
        feedback.textContent = self.strings.correct;
      } else {
        feedback.className = 'mb-4 rounded-lg px-4 py-3 text-sm bg-red-500/10 text-red-700 dark:text-red-400';
        feedback.textContent = self.strings.incorrect;
        if (result.answerText) {
          feedback.appendChild(el('div', 'mt-1 font-semibold whitespace-pre-wrap',
            self.strings.correct_answer + ' ' + result.answerText));
        }
      }
      if (q.explain) {
        feedback.appendChild(el('div', 'mt-2 text-stone-600 dark:text-stone-400', q.explain));
      }
      check.dataset.next = '1';
      check.textContent = self.strings.next;
      feedback.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
    });

    this.mount.appendChild(wrap);
  };

  Quiz.prototype.addCode = function (q, body) {
    if (!q.code) return;
    body.appendChild(el('pre', 'quiz-code', q.code));
  };

  // ---- single / truefalse / multi -------------------------------------------

  Quiz.prototype.buildChoice = function (q, body, onReady, checkBtn) {
    this.addCode(q, body);
    const multi = q.type === 'multi';
    const options = q.type === 'truefalse'
      ? [{ text: this.strings.true, value: true }, { text: this.strings.false, value: false }]
      : shuffled(q.options.map(function (text, i) { return { text: text, value: i }; }));

    const list = el('div', 'mt-3 space-y-2');
    const buttons = [];
    options.forEach(function (opt) {
      const btn = el('button', 'quiz-option', opt.text);
      btn.type = 'button';
      btn.dataset.value = String(opt.value);
      btn.addEventListener('click', function () {
        if (multi) {
          btn.classList.toggle('selected');
        } else {
          buttons.forEach(function (b) { b.classList.remove('selected'); });
          btn.classList.add('selected');
        }
        if (list.querySelector('.selected')) onReady();
        else checkBtn.disabled = true;
      });
      buttons.push(btn);
      list.appendChild(btn);
    });
    body.appendChild(list);

    const strings = this.strings;
    return function grade() {
      const picked = buttons.filter(function (b) { return b.classList.contains('selected'); });
      let correct;
      let answerText;
      if (q.type === 'truefalse') {
        correct = picked.length === 1 && picked[0].dataset.value === String(q.answer);
        answerText = q.answer ? strings.true : strings.false;
      } else if (multi) {
        const chosen = picked.map(function (b) { return Number(b.dataset.value); }).sort();
        const wanted = q.answers.slice().sort();
        correct = chosen.length === wanted.length &&
          chosen.every(function (v, i) { return v === wanted[i]; });
        answerText = q.answers.map(function (i) { return q.options[i]; }).join(', ');
      } else {
        correct = picked.length === 1 && Number(picked[0].dataset.value) === q.answer;
        answerText = q.options[q.answer];
      }
      buttons.forEach(function (b) {
        const v = b.dataset.value;
        const isRight = q.type === 'truefalse' ? v === String(q.answer)
          : multi ? q.answers.indexOf(Number(v)) !== -1
            : Number(v) === q.answer;
        if (isRight) b.classList.add('correct');
        else if (b.classList.contains('selected')) b.classList.add('wrong');
      });
      return { correct: correct, answerText: correct ? null : answerText };
    };
  };

  // ---- fill (type the answer) -----------------------------------------------

  Quiz.prototype.buildFill = function (q, body, onReady, checkBtn) {
    const pre = el('pre', 'quiz-code');
    const parts = (q.code || '__').split('__');
    const input = el('input', 'quiz-fill-input');
    input.type = 'text';
    input.autocapitalize = 'off';
    input.autocomplete = 'off';
    input.spellcheck = false;
    pre.appendChild(document.createTextNode(parts[0]));
    pre.appendChild(input);
    pre.appendChild(document.createTextNode(parts.slice(1).join('__')));
    body.appendChild(pre);

    input.addEventListener('input', function () {
      if (input.value.trim()) onReady();
      else checkBtn.disabled = true;
    });
    input.addEventListener('keydown', function (e) {
      if (e.key === 'Enter' && !checkBtn.disabled) {
        e.preventDefault();
        checkBtn.click();
      }
    });

    return function grade() {
      const given = input.value.trim().toLowerCase();
      const correct = q.accept.some(function (a) { return a.toLowerCase() === given; });
      input.classList.add(correct ? 'correct' : 'wrong');
      return { correct: correct, answerText: correct ? null : q.accept[0] };
    };
  };

  // ---- gap (tap words into blanks) -------------------------------------------

  Quiz.prototype.buildGap = function (q, body, onReady, checkBtn) {
    const pre = el('pre', 'quiz-code');
    const parts = q.code.split('__');
    const slots = [];
    parts.forEach(function (part, i) {
      pre.appendChild(document.createTextNode(part));
      if (i < parts.length - 1) {
        const slot = el('button', 'quiz-gap-slot');
        slot.type = 'button';
        slots.push(slot);
        pre.appendChild(slot);
      }
    });
    body.appendChild(pre);

    const bank = el('div', 'mt-3 flex flex-wrap gap-2');
    shuffled(q.bank).forEach(function (word) {
      const chip = el('button', 'quiz-chip', word);
      chip.type = 'button';
      chip.addEventListener('click', function () {
        if (chip.classList.contains('used')) return;
        const slot = slots.find(function (s) { return !s.dataset.word; });
        if (!slot) return;
        slot.dataset.word = word;
        slot.textContent = word;
        slot.classList.add('filled');
        slot._chip = chip;
        chip.classList.add('used');
        chip.disabled = true;
        if (slots.every(function (s) { return s.dataset.word; })) onReady();
      });
      bank.appendChild(chip);
    });
    body.appendChild(bank);

    slots.forEach(function (slot) {
      slot.addEventListener('click', function () {
        if (!slot.dataset.word) return;
        if (slot._chip) {
          slot._chip.classList.remove('used');
          slot._chip.disabled = false;
        }
        delete slot.dataset.word;
        slot.textContent = '';
        slot.classList.remove('filled');
        checkBtn.disabled = true;
      });
    });

    return function grade() {
      let correct = true;
      slots.forEach(function (slot, i) {
        const ok = slot.dataset.word === q.gaps[i];
        slot.classList.add(ok ? 'correct' : 'wrong');
        if (!ok) correct = false;
      });
      return { correct: correct, answerText: correct ? null : q.gaps.join(', ') };
    };
  };

  // ---- order (tap lines into order) -------------------------------------------

  Quiz.prototype.buildOrder = function (q, body, onReady, checkBtn) {
    const target = el('div', 'space-y-2 min-h-[2.5rem] rounded-lg border border-dashed border-stone-300 dark:border-stone-700 p-2');
    const pool = el('div', 'mt-3 space-y-2');
    body.appendChild(target);
    body.appendChild(pool);

    function refresh() {
      if (!pool.children.length) onReady();
      else checkBtn.disabled = true;
    }

    shuffled(q.items).forEach(function (item) {
      const btn = el('button', 'quiz-order-item', item);
      btn.type = 'button';
      btn.addEventListener('click', function () {
        (btn.parentElement === pool ? target : pool).appendChild(btn);
        refresh();
      });
      pool.appendChild(btn);
    });

    return function grade() {
      const placed = Array.prototype.map.call(target.children, function (n) { return n.textContent; });
      const correct = placed.length === q.items.length &&
        placed.every(function (v, i) { return v === q.items[i]; });
      Array.prototype.forEach.call(target.children, function (n, i) {
        n.classList.add(n.textContent === q.items[i] ? 'correct' : 'wrong');
      });
      return { correct: correct, answerText: correct ? null : q.items.join('\n') };
    };
  };

  // ---- results ----------------------------------------------------------------

  Quiz.prototype.renderResult = function () {
    this.clear();
    const percent = Math.round(this.score / this.questions.length * 100);
    const passed = percent >= this.passPercent;

    const wrap = el('div', 'text-center py-4');
    wrap.appendChild(el('p', 'text-sm font-semibold uppercase tracking-wide text-stone-400', this.strings.result_title));
    wrap.appendChild(el('p', 'mt-2 text-4xl font-bold tabular-nums', this.score + ' / ' + this.questions.length));
    const message = this.practice ? this.strings.result_practice
      : passed ? this.strings.result_passed : this.strings.result_failed;
    wrap.appendChild(el('p', 'mt-2 ' + (passed ? 'text-green-700 dark:text-green-400' : 'text-stone-600 dark:text-stone-400'), message));

    const retry = el('button', 'mt-5 ' + (passed ? BTN_SECONDARY : BTN_PRIMARY), this.strings.retry);
    retry.type = 'button';
    const self = this;
    retry.addEventListener('click', function () {
      self.reset();
      self.renderQuestion();
    });
    wrap.appendChild(retry);
    this.mount.appendChild(wrap);

    if (!this.practice && this.resultUrl) this.report(passed);
  };

  Quiz.prototype.report = function (passed) {
    const root = this.root;
    fetch(this.resultUrl, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-CSRF-Token': (document.querySelector('meta[name="csrf-token"]') || {}).content || '',
      },
      body: JSON.stringify({ score: this.score }),
      credentials: 'same-origin',
    }).then(function (r) { return r.ok ? r.json() : null; }).then(function (data) {
      if (data && data.passed) {
        root.dataset.quizPassed = '1';
        document.dispatchEvent(new CustomEvent('quiz:passed'));
      }
    }).catch(function () { /* results are best-effort; the quiz still works offline */ });
  };

  // ---- boot ---------------------------------------------------------------------

  function initQuizzes(scope) {
    (scope || document).querySelectorAll('[data-quiz]').forEach(function (root) {
      if (root.dataset.quizReady) return;
      root.dataset.quizReady = '1';
      const payload = root.querySelector('[data-quiz-payload]');
      if (!payload) return;
      try {
        new Quiz(root, JSON.parse(payload.textContent)).renderIntro();
      } catch (e) {
        // A malformed quiz should not break the lesson page.
      }
    });
  }

  initQuizzes();
  document.body.addEventListener('htmx:afterSwap', function () { initQuizzes(); });
})();
