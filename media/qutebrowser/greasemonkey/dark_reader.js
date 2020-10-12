// ==UserScript==
// @name          Dark Reader (Unofficial)
// @icon          https://darkreader.org/images/darkreader-icon-256x256.png
// @namespace     DarkReader
// @description	  Inverts the brightness of pages to reduce eye strain
// @version       4.7.15
// @author        https://github.com/darkreader/darkreader#contributors
// @homepageURL   https://darkreader.org/ | https://github.com/darkreader/darkreader
// @run-at        document-end
// @grant         none
// @include       http*
// @require       https://cdn.jsdelivr.net/npm/darkreader/darkreader.min.js
// @noframes
// @include	  qute*
// @exclude	  https://atom.io/*
// @exclude	  https://www.reddit.com/*
// @exclude	  https://www.youtube.com/*
// @exclude	  https://www.duckduckgo.com/*
// @exclude	  https://stackoverflow.com/*
// @exclude	  https://www.ghacks.net/*
// @exclude	  https://en.wikipedia.org/*
// ==/UserScript==

DarkReader.enable({
	brightness: 90,
	contrast: 90,
	sepia: 0
});
