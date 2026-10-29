/* Make the study dashboard the site's front page. Injected into the professor's root
 * index.html by en/tools/inject.py --home (one line, before his styles, so his page never
 * paints). index.html?upstream still shows his page, for maintenance. See CLAUDE.md. */
(function () {
  if (/[?&]upstream\b/.test(location.search)) return;
  location.replace('study/' + location.hash);
})();
