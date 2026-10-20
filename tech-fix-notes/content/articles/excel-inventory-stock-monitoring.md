---
title: Excel Inventory Sheet: Track Stock In and Out With Simple Formulas
description: Build an Excel stock monitoring sheet that updates automatically. Uses SUMIFS and IF formulas that work in Excel 2019 and newer, with a low-stock warning.
category: excel
date: 2026-10-15
---

You do not need special software to monitor stock. With three sheets and two formulas, Excel can show your **current stock**, mark items that need reordering, and update automatically every time you record an entry.

This guide uses **SUMIFS** and **IF**, which work in Excel 2010 and newer, including Excel 2019.

## What you will build

Three sheets in one workbook:

1. **Inventory**: one row per item, with the current stock calculated for you
2. **Stock In**: a log of everything received
3. **Stock Out**: a log of everything sold or used

## Step 1: Create the Inventory sheet

Rename a sheet to `Inventory` and set up these columns in row 1:

| A | B | C | D | E | F | G |
| --- | --- | --- | --- | --- | --- | --- |
| Item Code | Item Name | Reorder Level | Total In | Total Out | Current Stock | Status |

Fill in rows 2 and below with your item codes and names, and a reorder level for each (the number at which you want a warning).

For example:

| Item Code | Item Name | Reorder Level |
| --- | --- | --- |
| A001 | A4 Paper Ream | 10 |
| A002 | Black Ink Bottle | 5 |
| A003 | USB Cable | 8 |

## Step 2: Create the Stock In and Stock Out sheets

Create two sheets named `Stock In` and `Stock Out`. Use the same columns in both:

| A | B | C |
| --- | --- | --- |
| Date | Item Code | Quantity |

Every time you receive stock, add a new row in **Stock In**. Every time you sell or use stock, add a row in **Stock Out**.

If you already have stock on hand, enter it as your first **Stock In** entry, dated the day you start.

## Step 3: Add the formulas on the Inventory sheet

Click cell **D2** on the Inventory sheet and enter:

```
=SUMIFS('Stock In'!$C:$C,'Stock In'!$B:$B,$A2)
```

This adds up all quantities in Stock In for the item code in column A.

Click **E2** and enter:

```
=SUMIFS('Stock Out'!$C:$C,'Stock Out'!$B:$B,$A2)
```

Click **F2** and enter:

```
=D2-E2
```

Click **G2** and enter:

```
=IF(F2<=0,"OUT OF STOCK",IF(F2<=C2,"REORDER","OK"))
```

Select D2:G2 and drag the fill handle (the small square in the corner) down to copy the formulas to all your items.

## Step 4: Add a dropdown for item codes

This prevents typing mistakes that would break your totals.

1. Go to the **Stock In** sheet and select column B (from B2 downward).
2. Click **Data > Data Validation**.
3. Under **Allow**, choose **List**.
4. In **Source**, enter `=Inventory!$A$2:$A$200`.
5. Click OK. Repeat for the **Stock Out** sheet.

Now each entry uses a code from your Inventory list.

## Step 5: Highlight low stock automatically

1. On the Inventory sheet, select the **G** column data (G2 downward).
2. Click **Home > Conditional Formatting > Highlight Cells Rules > Text that Contains**.
3. Type `REORDER` and choose a yellow fill. Click OK.
4. Repeat for `OUT OF STOCK` with a red fill and `OK` with a green fill.

## Step 6: Show the item name automatically on the log sheets (optional)

On the **Stock In** sheet, add a column D with the heading **Item Name**. In D2 enter:

```
=IFERROR(VLOOKUP(B2,Inventory!$A:$B,2,FALSE),"")
```

Copy it down. The name now appears when you pick a code. Use `VLOOKUP` rather than `XLOOKUP` if you use Excel 2019, because `XLOOKUP` is only available in newer versions (Excel 2021 and Microsoft 365).

## Step 7: Add the stock value (optional)

Add a **Unit Cost** column in Inventory (for example, column H) and a **Stock Value** column (column I) with:

```
=F2*H2
```

At the bottom, a total is simply:

```
=SUM(I2:I200)
```

## Tips to avoid mistakes

- Keep item codes **unique** and never reuse a code for a different item
- Do not type over formulas. Select and **protect** the formula columns using **Review > Protect Sheet**
- Format your log entries as a **Table** (Insert > Table) so the ranges grow as you add rows
- Back up the file regularly (copy it to a cloud drive or flash drive)
- Record entries the same day to keep numbers accurate

## Common problems

**The totals show 0 even though I made entries.**
Check that item codes match exactly. A trailing space or a lowercase letter will break the match. The dropdown from Step 4 prevents this.

**Stock goes negative.**
Someone recorded more going out than was ever received. Check your Stock Out entries and any missing Stock In entries.

**Formulas show as text.**
The cell is formatted as Text. Change the format to **General** and re-enter the formula.

Want a ready-made template or a version with monthly reports? Tell me on the [Contact page](../contact.html) what you need.
