// ==UserScript==
// @require  file:///home/boris/.local/share/qutebrowser/greasemonkey/keydrown.js
// @include  http*
// @include	 http://127.0.0.1:8081/*
// @include  qute*
// @include  https://www.youtube.com/*
// ==/UserScript==

kd.J.down(function () {
  if (window.qutebrowserMode === 'normal') {
    window.scrollBy({
      top: 20,
      left: 0,
      behavior: 'smooth'});
  }
});

kd.K.down(function () {
  if (window.qutebrowserMode === 'normal') {
    window.scrollBy({
      top: -20,
      left: 0,
      behavior: 'smooth'});
  }
});

kd.D.down(function () {
  if (window.qutebrowserMode === 'normal') {
    window.scrollBy({
      top: 80,
      left: 0,
      behavior: 'smooth'});
  }
});

kd.E.down(function () {
  if (window.qutebrowserMode === 'normal') {
    window.scrollBy({
      top: -80,
      left: 0,
      behavior: 'smooth'});
  }
});

kd.run(function () {
  kd.tick();
});

document.addEventListener('keypress', (event) => {
  if (( event.key === 'j' || event.key === 'k' || event.key === 'e' || event.key === 'd' ) && ( window.qutebrowserMode === "normal" )) {
    event.preventDefault();
  }
});

window.eval('window.qutebrowserMode = "normal";');
