// themeToggle.js
function toggleTheme() {
  const body = document.body;
  const currentTheme = body.getAttribute('data-bs-theme');
  const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
  body.setAttribute('data-bs-theme', newTheme);
  localStorage.setItem('theme', newTheme);
}

// načtení uloženého motivu
window.addEventListener('DOMContentLoaded', () => {
  const savedTheme = localStorage.getItem('theme') || 'light';
  document.body.setAttribute('data-bs-theme', savedTheme);
});
