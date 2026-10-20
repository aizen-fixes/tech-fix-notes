# Tech Fix Notes: your own troubleshooting website

A fast, simple, free-to-host website for tutorials and troubleshooting guides, ready for Google AdSense.
No WordPress, no database, no monthly fees. You write articles as plain text files, and one command turns them into a website.

**Included:** home page, 4 topic categories, 5 starter articles, search box, About, Contact, Privacy Policy and Disclaimer pages, mobile layout, dark mode, sitemap, robots.txt and ads.txt (created for you once you set your settings).

## What is in this folder

| Path | What it is |
| --- | --- |
| `site/` | **The finished website.** Upload this folder to a host. |
| `config.json` | Your settings: site name, pen name, contact form, AdSense ID |
| `content/articles/` | Your articles (one `.md` text file each) |
| `content/pages/` | About, Contact, Privacy Policy, Disclaimer |
| `content/images/` | Your screenshots and photos |
| `build.py` | Builds the website into `site/` |
| `new_article.py` | Creates a new article from a template |
| `IDEAS.md` | 45 article ideas, title formula and a quality checklist |

## Step 1: Look at the site on your computer

Open `site/index.html` by double-clicking it. Everything works offline, including the search.

## Step 2: Put it online for free

Upload the **contents of the `site` folder** (the folder that contains `index.html`) to any free static host. Any of these work:

- **Netlify**: sign up, then drag the `site` folder onto the "Deploy" area on the Netlify Drop page
- **Cloudflare Pages**: create a project and choose Direct Upload
- **GitHub Pages**: upload the files to a repository and turn on Pages

The host screens change from time to time, so follow each host's current instructions.

**Upload only the `site` folder (or the `tech-fix-notes-site-only.zip` file), not the whole project.** If you upload the whole project, the host may try to run `build.py` itself and show a "Build script returned non-zero exit code" error. The `site` folder is already built, so it needs no build step.

### Important: AdSense needs your own domain

The free addresses (`yourname.netlify.app`, `yourname.pages.dev`, `yourname.github.io`) are fine for testing, but AdSense wants a site you own, and approval on a shared host address is unlikely. Buy a domain (for example `techfixnotes.com`, usually around $10 to $15 a year for a .com) and connect it in your host's **Domain settings**. Hosting stays free.

Turn on **domain privacy (WHOIS privacy)** when you buy it, so your real name and address are not published. Most registrars offer it free or cheap.

## Step 3: Set up the contact form (keeps your email private)

1. In Google Forms, create a form with Name, Email and Message (you already started one).
2. Click the three dots and choose **Embed HTML**. Copy only the address inside `src="..."`.
3. Paste it into `config.json` as `contact_form_url`.
4. Leave `contact_email` empty so no email address is shown.

## Step 4: Change your settings

Open `config.json` in Notepad (or any text editor):

| Setting | What to put |
| --- | --- |
| `site_name` | Your site name |
| `author_name` | The name shown on articles. Use a pen name if you want to stay anonymous |
| `site_url` | Your domain, for example `https://techfixnotes.com` (leave empty until you have one) |
| `contact_form_url` | The Google Form address from Step 3 |
| `adsense_publisher_id` | Your AdSense ID, like `ca-pub-1234567890123456` (see Step 7) |
| `adsense_article_slot` | Optional ad unit ID for one ad inside each article |

## Step 5: Add and edit articles

You need Python 3 installed (python.org) and the one-time command `pip install markdown`.

    python3 new_article.py "Printer Prints Blank Pages? What to Check" printers
    (open content/articles/printer-prints-blank-pages-what-to-check.md and write it)
    python3 build.py

Then upload the `site` folder again. On Windows, use `python` instead of `python3` if needed.

Article files start with a small header between `---` lines (title, description, category, date), followed by your text. Use `## Heading` for sections, `1.` for numbered steps and `![caption](../images/file.png)` for pictures.

Categories are `printers`, `windows-pc`, `excel` and `networking`. You can add or rename them in `config.json`.

## Step 6: Make the starter articles yours

The 5 starter articles are solid general guides, but **AdSense rewards original, helpful content**. Before you apply:

- Add **your own screenshots and photos** to every article
- Add a short paragraph from **your real experience** ("I fixed this on a client's printer when...")
- Fix any step that is different on the devices you work with
- Do not copy text from other sites

## Step 7: Apply for AdSense

1. Reach **15 to 25 original articles** and keep the About, Contact, Privacy Policy and Disclaimer pages. Have the site on **your own domain**.
2. Sign in to AdSense with your Google account and add your site. AdSense asks for your real name and address for payments. This stays private and is never shown to visitors.
3. Copy your publisher ID (it starts with `ca-pub-`) into `adsense_publisher_id` in `config.json`.
4. Run `python3 build.py` and upload `site` again. This puts the AdSense code on every page and creates `ads.txt`.
5. In AdSense, click verify. Approval can take days to a few weeks.
6. After approval, turn on **Auto ads** in AdSense, or create a display ad unit and put its ID in `adsense_article_slot`.

Rules to remember: never click your own ads, never ask others to click them, and keep your content original and honest.

## Troubleshooting

- **"Missing dependency"**: run `pip install markdown`
- **"unknown category"**: use one of the category names listed in `config.json`
- **Images do not show**: the file must be in `content/images/`, and the link must start with `../images/`
- **Changes not showing online**: you must run `python3 build.py` and upload `site` again
