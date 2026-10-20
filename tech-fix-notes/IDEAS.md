# Article ideas for Tech Fix Notes

Aim for **15 to 25 original articles** before you apply for AdSense, then keep publishing 2 to 4 a week.
Create each one with:

    python3 new_article.py "Your article title" printers

## The title formula

**Exact problem + the model or error name + a promise of the fix.**

- Good: "Epson L3210 Shows Paper Out but Paper Is Loaded? Try This Fix First"
- Good: "Windows 10 No Internet but Wi-Fi Connected? 6 Fixes That Work"
- Avoid: "You Won't Believe What This Printer Did!" (it hides the problem, so people leave)

People search for the exact error text, so put it in the title and the first paragraph.

## Where to find ideas that people really search for

1. **Your own work.** Every problem you fixed for a client or coworker this month is an article.
2. **Google autocomplete.** Type "epson printer" and see what Google suggests. Each suggestion is a real search.
3. **"People also ask"** boxes under search results.
4. **Questions on forums** (Microsoft Community, printer brand forums, Reddit tech support). Write the guide you wish they had found.
5. **Error codes and messages.** One article per exact message tends to do well.
6. **Comments and contact form messages** from your readers.

## Topic backlog

### Printers
- Printer has ink but prints blank pages
- Printer says paper jam but there is no paper
- Printer offline in Windows 10/11: how to bring it back online
- How to install a printer driver correctly
- Printer prints with lines or streaks: how to clean the print head
- How to clean the print head on an EcoTank-style printer
- Printer will not connect to Wi-Fi after changing the router
- Printer prints very slowly: causes and fixes
- Print queue stuck: how to clear it
- Printer prints the wrong colors
- How to share a printer on a local network
- How to scan to a computer from a multifunction printer

### Windows and PC
- Computer won't turn on: what to check first
- Blue screen of death: how to find the cause
- Windows 11 slow after update: 6 things to try
- How to free up disk space on Windows
- Laptop battery drains fast: fixes and settings
- Laptop keyboard not working: quick checks
- USB device not recognized: how to fix it
- Computer keeps restarting by itself
- Computer overheating and fan too loud
- How to reset a Windows password you forgot (on your own PC)
- No sound on computer: step-by-step fixes
- How to clean a dusty desktop PC safely

### Excel tutorials
- VLOOKUP vs XLOOKUP: which should you use?
- How to remove duplicates in Excel
- Excel IF formula for beginners, with examples
- How to make a monthly expense tracker in Excel
- How to make a simple attendance sheet in Excel
- SUMIF and SUMIFS explained with examples
- Excel drop-down list: how to create one
- How to protect formulas in Excel so they cannot be edited
- How to make a price list that updates automatically
- Pivot tables for beginners
- How to fix "#N/A", "#VALUE!" and "#REF!" errors in Excel

### Networking
- Wi-Fi connected but no internet: fixes that work
- How to find your router's IP address and log in
- How to change your Wi-Fi password
- How to set up a printer or file sharing on a home LAN
- How to fix "Limited connectivity" in Windows
- How to check who is using your Wi-Fi
- Slow internet: how to test and what to change
- How to set up a static IP address
- What do the lights on a router mean?
- How to crimp an RJ45 network cable

## Quality checklist before you publish

- [ ] The title contains the exact problem or error
- [ ] The first paragraph says what the reader will fix and how long it takes
- [ ] The easiest fix comes first
- [ ] Steps are numbered and each one is a single action
- [ ] At least one **real screenshot or photo of your own** (put files in `content/images/`)
- [ ] You tested the steps yourself or have solved this problem before
- [ ] A "when to call a technician" section
- [ ] A short FAQ with 2 to 3 questions
- [ ] 800+ words for guides, shorter is fine for very specific error codes
- [ ] No copied text from other websites, and no text pasted from an AI tool without your own edits and experience

## Adding a screenshot

1. Save the image in `content/images/` (for example `epson-paper-out.png`). Keep file sizes small (under 300 KB).
2. In the article, add:

       ![Epson control panel showing the Paper Out light](../images/epson-paper-out.png)

3. Rebuild with `python3 build.py`.
