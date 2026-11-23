// The reading pages: a contents rail built from the page's own headings,
// marking the section being read. Ids already in the page are kept.
(function () {
  var doc = document.querySelector('.doc'), rail = document.querySelector('.toc');
  if (!doc || !rail) return;
  var heads = [].slice.call(doc.querySelectorAll('h2'));
  if (heads.length < 3) { rail.remove(); return; }
  var used = {};
  [].forEach.call(document.querySelectorAll('[id]'), function (el) { used[el.id] = 1; });
  var ol = document.createElement('ol'), links = [];
  heads.forEach(function (h) {
    if (!h.id) {
      var base = h.textContent.toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '') || 'section', id = base, n = 2;
      while (used[id]) id = base + '-' + n++;
      used[id] = 1; h.id = id;
    }
    var li = document.createElement('li'), a = document.createElement('a');
    a.href = '#' + h.id; a.textContent = h.textContent;
    li.appendChild(a); ol.appendChild(li); links.push(a);
  });
  rail.appendChild(ol);
  function mark() {
    var cur = 0;
    for (var i = 0; i < heads.length; i++) if (heads[i].getBoundingClientRect().top < 140) cur = i;
    links.forEach(function (a, i) { a.classList.toggle('on', i === cur); });
  }
  mark();
  window.addEventListener('scroll', mark, { passive: true });
})();
