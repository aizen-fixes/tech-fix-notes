#!/usr/bin/env python3
"""
Tech Fix Notes - tiny static site generator.

Usage:   python3 build.py
Output:  the finished website in the "site" folder (upload that folder to any free host).

Articles live in content/articles/*.md, pages in content/pages/*.md.
Settings (site name, AdSense ID, contact form...) live in config.json.
"""
import datetime
import html
import json
import re
import shutil
import sys
from pathlib import Path

try:
    import markdown
except ImportError:
    sys.exit("Missing dependency. Run:  pip install markdown")

BASE = Path(__file__).resolve().parent
CONTENT = BASE / "content"
STATIC = BASE / "static"
OUT = BASE / "site"

CFG = json.loads((BASE / "config.json").read_text(encoding="utf-8"))
CATS = {c["slug"]: c for c in CFG["categories"]}
SITE_URL = CFG.get("site_url", "").rstrip("/")
PUB_ID = CFG.get("adsense_publisher_id", "").strip()
AD_SLOT = CFG.get("adsense_article_slot", "").strip()


# ---------------------------------------------------------------- helpers
def esc(s):
    return html.escape(str(s), quote=True)


def parse_file(path):
    """Read a markdown file with a simple '---' front matter block."""
    text = path.read_text(encoding="utf-8")
    meta, body = {}, text
    if text.startswith("---"):
        parts = text.split("---", 2)
        if len(parts) == 3:
            for line in parts[1].strip().splitlines():
                if ":" in line:
                    key, val = line.split(":", 1)
                    meta[key.strip().lower()] = val.strip().strip('"').strip("'")
            body = parts[2]
    return meta, body.strip()


def render_md(body):
    md = markdown.Markdown(extensions=["extra", "sane_lists", "toc"])
    return md.convert(body)


def plain_text(html_text):
    text = re.sub(r"<[^>]+>", " ", html_text)
    return re.sub(r"\s+", " ", html.unescape(text)).strip()


def read_minutes(html_text):
    words = len(plain_text(html_text).split())
    return max(1, round(words / 200))


def pretty_date(iso):
    try:
        d = datetime.date.fromisoformat(iso)
        return d.strftime("%B %d, %Y").replace(" 0", " ")
    except ValueError:
        return iso


def abs_url(rel):
    return f"{SITE_URL}/{rel}" if SITE_URL else ""


def write(rel_path, content):
    target = OUT / rel_path
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(content, encoding="utf-8")


# ---------------------------------------------------------------- layout
def adsense_head():
    if not PUB_ID:
        return ""
    return (
        '<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js'
        f'?client={esc(PUB_ID)}" crossorigin="anonymous"></script>'
    )


def ad_unit():
    """Optional manual ad slot (only if a slot ID is set in config.json)."""
    if not (PUB_ID and AD_SLOT):
        return ""
    return (
        '<div class="ad-wrap"><span class="ad-label">Advertisement</span>'
        f'<ins class="adsbygoogle" style="display:block" data-ad-client="{esc(PUB_ID)}" '
        f'data-ad-slot="{esc(AD_SLOT)}" data-ad-format="auto" data-full-width-responsive="true"></ins>'
        '<script>(adsbygoogle = window.adsbygoogle || []).push({});</script></div>'
    )


def header(root):
    cat_links = "".join(
        f'<a href="{root}category/{c["slug"]}.html">{esc(c["name"])}</a>' for c in CFG["categories"]
    )
    return f"""
<header class="site-header">
  <div class="wrap header-inner">
    <a class="brand" href="{root}index.html">{esc(CFG['site_name'])}</a>
    <button class="nav-toggle" aria-label="Menu" onclick="document.body.classList.toggle('nav-open')">&#9776;</button>
    <nav class="main-nav">
      {cat_links}
      <a href="{root}about.html">About</a>
      <a href="{root}contact.html">Contact</a>
    </nav>
    <form class="search-mini" action="{root}search.html" method="get" role="search">
      <input type="search" name="q" placeholder="Search fixes..." aria-label="Search">
    </form>
  </div>
</header>"""


def footer(root):
    year = datetime.date.today().year
    return f"""
<footer class="site-footer">
  <div class="wrap">
    <p><strong>{esc(CFG['site_name'])}</strong> &mdash; {esc(CFG['tagline'])}</p>
    <p class="footer-links">
      <a href="{root}about.html">About</a>
      <a href="{root}contact.html">Contact</a>
      <a href="{root}privacy-policy.html">Privacy Policy</a>
      <a href="{root}disclaimer.html">Disclaimer</a>
    </p>
    <p class="small">&copy; {year} {esc(CFG['site_name'])}. All rights reserved.</p>
  </div>
</footer>"""


def layout(title, description, body, root="", path="", og_type="website", jsonld=None, noindex=False):
    full_title = title if title == CFG["site_name"] else f"{title} | {CFG['site_name']}"
    canonical = f'<link rel="canonical" href="{esc(abs_url(path))}">' if (SITE_URL and path) else ""
    og_url = f'<meta property="og:url" content="{esc(abs_url(path))}">' if (SITE_URL and path) else ""
    ld = f'<script type="application/ld+json">{json.dumps(jsonld)}</script>' if jsonld else ""
    robots = '<meta name="robots" content="noindex">' if noindex else ""
    return f"""<!doctype html>
<html lang="{esc(CFG.get('language', 'en'))}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(full_title)}</title>
<meta name="description" content="{esc(description)}">
{robots}
{canonical}
<meta property="og:title" content="{esc(full_title)}">
<meta property="og:description" content="{esc(description)}">
<meta property="og:type" content="{og_type}">
<meta property="og:site_name" content="{esc(CFG['site_name'])}">
{og_url}
<link rel="stylesheet" href="{root}static/style.css">
{adsense_head()}
{ld}
</head>
<body>
{header(root)}
<main class="wrap">
{body}
</main>
{footer(root)}
</body>
</html>"""


def article_card(a, root):
    cat = CATS.get(a["category"], {"name": a["category"]})
    return f"""
<article class="card">
  <span class="tag">{esc(cat['name'])}</span>
  <h3><a href="{root}articles/{a['slug']}.html">{esc(a['title'])}</a></h3>
  <p>{esc(a['description'])}</p>
  <p class="meta">{pretty_date(a['date'])} &middot; {a['minutes']} min read</p>
</article>"""


# ---------------------------------------------------------------- load content
def load_articles():
    items = []
    for f in sorted((CONTENT / "articles").glob("*.md")):
        meta, body = parse_file(f)
        for key in ("title", "description", "category", "date"):
            if key not in meta:
                sys.exit(f"{f.name}: missing '{key}' in the front matter")
        if meta["category"] not in CATS:
            sys.exit(f"{f.name}: unknown category '{meta['category']}'. Use one of: {', '.join(CATS)}")
        content_html = render_md(body)
        items.append(
            {
                "slug": f.stem,
                "title": meta["title"],
                "description": meta["description"],
                "category": meta["category"],
                "date": meta["date"],
                "updated": meta.get("updated", meta["date"]),
                "html": content_html,
                "minutes": read_minutes(content_html),
            }
        )
    items.sort(key=lambda a: a["date"], reverse=True)
    return items


def load_pages():
    pages = {}
    for f in sorted((CONTENT / "pages").glob("*.md")):
        meta, body = parse_file(f)
        pages[f.stem] = {
            "slug": f.stem,
            "title": meta.get("title", f.stem.title()),
            "description": meta.get("description", CFG["description"]),
            "html": render_md(body),
        }
    return pages


# ---------------------------------------------------------------- page builders
def build_home(articles):
    cats = "".join(
        f'<a class="cat-card" href="category/{c["slug"]}.html"><strong>{esc(c["name"])}</strong>'
        f'<span>{esc(c["description"])}</span></a>'
        for c in CFG["categories"]
    )
    latest = "".join(article_card(a, "") for a in articles[:9])
    body = f"""
<section class="hero">
  <h1>{esc(CFG['tagline'])}</h1>
  <p>{esc(CFG['description'])}</p>
  <form class="search-big" action="search.html" method="get" role="search">
    <input type="search" name="q" placeholder="Type your problem, e.g. printer paper out" aria-label="Search">
    <button type="submit">Search</button>
  </form>
</section>
<section>
  <h2>Browse by topic</h2>
  <div class="cat-grid">{cats}</div>
</section>
<section>
  <h2>Latest guides</h2>
  <div class="grid">{latest}</div>
</section>"""
    website_ld = {
        "@context": "https://schema.org",
        "@type": "WebSite",
        "name": CFG["site_name"],
        "description": CFG["description"],
    }
    if SITE_URL:
        website_ld["url"] = SITE_URL + "/"
    write("index.html", layout(CFG["site_name"], CFG["description"], body, "", "", jsonld=website_ld))


def build_article(a, articles):
    root = "../"
    cat = CATS[a["category"]]
    related = [x for x in articles if x["slug"] != a["slug"] and x["category"] == a["category"]][:3]
    if len(related) < 3:
        extra = [x for x in articles if x["slug"] != a["slug"] and x not in related]
        related += extra[: 3 - len(related)]
    related_html = ""
    if related:
        related_html = '<section class="related"><h2>More guides you may need</h2><div class="grid">' + "".join(
            article_card(r, root) for r in related
        ) + "</div></section>"

    # drop an optional ad after the first paragraph
    content = a["html"]
    unit = ad_unit()
    if unit and "</p>" in content:
        content = content.replace("</p>", "</p>" + unit, 1)

    body = f"""
<nav class="crumbs" aria-label="Breadcrumb">
  <a href="{root}index.html">Home</a> &rsaquo;
  <a href="{root}category/{cat['slug']}.html">{esc(cat['name'])}</a> &rsaquo;
  <span>{esc(a['title'])}</span>
</nav>
<article class="post">
  <h1>{esc(a['title'])}</h1>
  <p class="meta">By {esc(CFG['author_name'])} &middot; {pretty_date(a['date'])} &middot; {a['minutes']} min read</p>
  <div class="prose">{content}</div>
  <aside class="help-box">
    <strong>Still stuck?</strong> Tell me your device model, your operating system and the exact error message on the
    <a href="{root}contact.html">Contact page</a> and I will try to help.
  </aside>
</article>
{related_html}"""
    ld = {
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": a["title"],
        "description": a["description"],
        "datePublished": a["date"],
        "dateModified": a["updated"],
        "author": {"@type": "Person", "name": CFG["author_name"]},
        "publisher": {"@type": "Organization", "name": CFG["site_name"]},
    }
    path = f"articles/{a['slug']}.html"
    write(path, layout(a["title"], a["description"], body, root, path, "article", ld))


def build_category(cat, articles):
    root = "../"
    items = [a for a in articles if a["category"] == cat["slug"]]
    cards = "".join(article_card(a, root) for a in items) or "<p>No guides here yet. Check back soon!</p>"
    body = f"""
<nav class="crumbs"><a href="{root}index.html">Home</a> &rsaquo; <span>{esc(cat['name'])}</span></nav>
<h1>{esc(cat['name'])}</h1>
<p class="lead">{esc(cat['description'])}</p>
<div class="grid">{cards}</div>"""
    path = f"category/{cat['slug']}.html"
    write(path, layout(cat["name"], cat["description"], body, root, path))


def build_page(p):
    extra = ""
    if p["slug"] == "contact":
        form = CFG.get("contact_form_url", "").strip()
        email = CFG.get("contact_email", "").strip()
        if form:
            extra += (
                f'<iframe class="form-frame" src="{esc(form)}" width="100%" height="820" '
                'frameborder="0" marginheight="0" marginwidth="0">Loading form...</iframe>'
            )
        if email:
            extra += f'<p>You can also email me at <a href="mailto:{esc(email)}">{esc(email)}</a>.</p>'
        if not extra:
            extra = (
                '<p class="notice">The contact form is not connected yet. '
                "Add your Google Form link as <code>contact_form_url</code> in config.json and rebuild.</p>"
            )
    body = f"""
<article class="post">
  <h1>{esc(p['title'])}</h1>
  <div class="prose">{p['html']}{extra}</div>
</article>"""
    path = f"{p['slug']}.html"
    write(path, layout(p["title"], p["description"], body, "", path))


def build_search(articles):
    body = """
<h1>Search</h1>
<form class="search-big" action="search.html" method="get" role="search">
  <input id="search-input" type="search" name="q" placeholder="Type your problem..." aria-label="Search" autofocus>
  <button type="submit">Search</button>
</form>
<p id="search-status" class="meta"></p>
<div id="search-results" class="grid"></div>
<script src="search-index.js"></script>
<script src="static/search.js"></script>"""
    write("search.html", layout("Search", "Search all troubleshooting guides.", body, "", "search.html", noindex=True))

    index = []
    for a in articles:
        index.append(
            {
                "title": a["title"],
                "description": a["description"],
                "category": CATS[a["category"]]["name"],
                "url": f"articles/{a['slug']}.html",
                "date": a["date"],
                "text": plain_text(a["html"])[:3000],
            }
        )
    write("search-index.js", "window.SEARCH_INDEX = " + json.dumps(index) + ";")


def build_404():
    body = """
<article class="post">
  <h1>Page not found</h1>
  <p>Sorry, that page does not exist. Try searching for your problem or go back to the home page.</p>
  <form class="search-big" action="/search.html" method="get"><input type="search" name="q" placeholder="Search..."><button>Search</button></form>
  <p><a href="/index.html">&larr; Back to home</a></p>
</article>"""
    # the 404 page can be served from any folder depth, so it uses root-absolute links ("/")
    write("404.html", layout("Page not found", "Page not found", body, "/", "", noindex=True))


def build_seo_files(articles, pages):
    if SITE_URL:
        urls = ["index.html"]
        urls += [f"category/{c['slug']}.html" for c in CFG["categories"]]
        urls += [f"{slug}.html" for slug in pages]
        urls += [f"articles/{a['slug']}.html" for a in articles]
        today = datetime.date.today().isoformat()
        rows = "".join(f"<url><loc>{esc(abs_url(u))}</loc><lastmod>{today}</lastmod></url>" for u in urls)
        write(
            "sitemap.xml",
            '<?xml version="1.0" encoding="UTF-8"?>'
            f'<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{rows}</urlset>',
        )
        write("robots.txt", f"User-agent: *\nAllow: /\n\nSitemap: {SITE_URL}/sitemap.xml\n")
    else:
        write("robots.txt", "User-agent: *\nAllow: /\n")
    if PUB_ID:
        pub = PUB_ID.replace("ca-", "", 1)
        write("ads.txt", f"google.com, {pub}, DIRECT, f08c47fec0942fa0\n")


# ---------------------------------------------------------------- main
def main():
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir()
    shutil.copytree(STATIC, OUT / "static")
    if (CONTENT / "images").exists():
        shutil.copytree(CONTENT / "images", OUT / "images")

    articles = load_articles()
    pages = load_pages()

    build_home(articles)
    for a in articles:
        build_article(a, articles)
    for c in CFG["categories"]:
        build_category(c, articles)
    for p in pages.values():
        build_page(p)
    build_search(articles)
    build_404()
    build_seo_files(articles, pages)

    print(f"Built {len(articles)} articles, {len(pages)} pages -> {OUT}")
    if not SITE_URL:
        print("Note: site_url is empty, so no sitemap.xml was created. Set it after you get your domain.")
    if not PUB_ID:
        print("Note: adsense_publisher_id is empty, so no ads are included yet.")


if __name__ == "__main__":
    main()
