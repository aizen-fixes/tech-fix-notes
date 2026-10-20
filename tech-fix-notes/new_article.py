#!/usr/bin/env python3
"""
Create a new article file from a template.

Usage:
    python3 new_article.py "Printer Prints Blank Pages? What to Check" printers

Categories: printers, windows-pc, excel, networking (see config.json)
Then open the new file in content/articles/, fill it in, and run:  python3 build.py
"""
import datetime
import json
import re
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parent
cfg = json.loads((BASE / "config.json").read_text(encoding="utf-8"))
cats = [c["slug"] for c in cfg["categories"]]

if len(sys.argv) < 3:
    sys.exit(f'Usage: python3 new_article.py "Article title" <category>\nCategories: {", ".join(cats)}')

title, category = sys.argv[1], sys.argv[2]
if category not in cats:
    sys.exit(f"Unknown category '{category}'. Choose one of: {', '.join(cats)}")

slug = re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")[:70]
path = BASE / "content" / "articles" / f"{slug}.md"
if path.exists():
    sys.exit(f"{path.name} already exists")

template = f"""---
title: {title}
description: Write 1-2 sentences (under 160 characters) that say what problem this fixes.
category: {category}
date: {datetime.date.today().isoformat()}
---

Start with the problem in your reader's words. Say what they see (the error message, the symptom).

## Why it happens

Explain the most common causes in plain language.

## Fix 1: The quickest fix

1. Step one.
2. Step two.

> Add a warning here if a step can lose data or damage hardware.

![Describe the screenshot](../images/your-screenshot.png)

## Fix 2: The next fix

## When to call a technician

## Frequently asked questions

**Question?**
Short answer.

Still stuck? Send me the details on the [Contact page](../contact.html).
"""
path.write_text(template, encoding="utf-8")
print(f"Created {path.relative_to(BASE)}")
print("Edit it, then run: python3 build.py")
