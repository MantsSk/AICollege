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
