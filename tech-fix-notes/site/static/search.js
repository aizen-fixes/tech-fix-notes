(function () {
  var box = document.getElementById("search-results");
  var input = document.getElementById("search-input");
  var status = document.getElementById("search-status");
  if (!box || !window.SEARCH_INDEX) return;

  function esc(s) {
    return String(s).replace(/[&<>"']/g, function (c) {
      return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c];
    });
  }

  function score(doc, terms) {
    var title = doc.title.toLowerCase();
    var cat = doc.category.toLowerCase();
    var desc = doc.description.toLowerCase();
    var text = doc.text.toLowerCase();
    var total = 0;
    for (var i = 0; i < terms.length; i++) {
      var t = terms[i];
      var hit = 0;
      if (title.indexOf(t) !== -1) hit += 5;
      if (cat.indexOf(t) !== -1) hit += 3;
      if (desc.indexOf(t) !== -1) hit += 2;
      if (text.indexOf(t) !== -1) hit += 1;
      if (hit === 0) return 0; // every word must match somewhere
      total += hit;
    }
    return total;
  }

  function render(q) {
    q = q.trim().toLowerCase();
    if (!q) {
      box.innerHTML = "";
      status.textContent = "Type a few words about your problem.";
      return;
    }
    var terms = q.split(/\s+/).filter(function (t) { return t.length > 1; });
    if (!terms.length) terms = [q];
    var results = window.SEARCH_INDEX
      .map(function (d) { return { d: d, s: score(d, terms) }; })
      .filter(function (r) { return r.s > 0; })
      .sort(function (a, b) { return b.s - a.s; });

    status.textContent = results.length
      ? results.length + " guide" + (results.length > 1 ? "s" : "") + " found"
      : "No guides found. Try different words, or ask on the Contact page and I may write one.";

    box.innerHTML = results.map(function (r) {
      var d = r.d;
      return '<article class="card"><span class="tag">' + esc(d.category) + "</span>" +
        '<h3><a href="' + esc(d.url) + '">' + esc(d.title) + "</a></h3>" +
        "<p>" + esc(d.description) + "</p></article>";
    }).join("");
  }

  var params = new URLSearchParams(window.location.search);
  var initial = params.get("q") || "";
  if (input) {
    input.value = initial;
    input.addEventListener("input", function () { render(input.value); });
  }
  render(initial);
})();
