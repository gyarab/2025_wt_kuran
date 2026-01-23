// themeToggle.js
function toggleTheme() {
  const htmlEl = document.documentElement;
  const currentTheme = htmlEl.getAttribute('data-theme') || 'light';
  const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
  htmlEl.setAttribute('data-theme', newTheme);
  localStorage.setItem('theme', newTheme);
}

// načtení uloženého motivu
window.addEventListener('DOMContentLoaded', () => {
  const savedTheme = localStorage.getItem('theme') || 'light';
  document.documentElement.setAttribute('data-theme', savedTheme);
});
