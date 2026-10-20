---
title: Computer Running Slow? 7 Free Fixes to Try Today
description: Slow Windows PC? These 7 free fixes, from startup programs to disk cleanup and system file repair, can speed it up without buying anything.
category: windows-pc
date: 2026-10-15
---

A slow computer is frustrating, but it rarely means the machine is dead. Most slowdowns come from too many programs starting with Windows, a nearly full drive, or background tasks using all the memory.

Try these fixes in order. They are free and safe if you follow the steps.

## Fix 1: Restart the computer

It sounds too simple, but a restart clears memory and stops stuck background processes. If you usually use sleep or hibernate, your PC may have been running for weeks. Do a full **Restart** (not Shut down, which can use fast startup).

## Fix 2: Find what is using your resources

1. Press **Ctrl + Shift + Esc** to open Task Manager.
2. Click the **Processes** tab.
3. Click the **CPU**, **Memory** and **Disk** headings to sort by usage.
4. If one program is using most of the CPU, memory or disk, close it. Right-click it and choose **End task**.

Do not end tasks you do not recognize, especially those named after Windows, until you check what they are.

## Fix 3: Turn off startup programs

Too many apps launching at startup is a top cause of slow boots.

1. In Task Manager, click the **Startup apps** tab.
2. Sort by **Startup impact**.
3. Right-click apps you do not need immediately (chat apps, updaters, music players) and choose **Disable**.

This does not uninstall anything. You can enable them again later.

## Fix 4: Free up disk space

Windows slows down when the system drive is nearly full. Try to keep at least **15 to 20 percent free**.

1. Open **Settings > System > Storage**.
2. Turn on **Storage Sense** or click **Temporary files** and delete what you do not need (such as temporary files and the Recycle Bin).
3. Click **Apps** (or **Installed apps**) and uninstall programs you no longer use.
4. Move large photos and videos to an external drive or cloud storage.

## Fix 5: Scan for malware

Malware and unwanted programs can slow everything down.

1. Open **Windows Security** from the Start menu.
2. Choose **Virus & threat protection > Scan options**.
3. Select **Full scan** and click **Scan now**.

A full scan can take an hour or more, so run it when you do not need the computer.

## Fix 6: Update Windows and drivers

1. Open **Settings > Windows Update** and install all available updates, then restart.
2. For graphics and chipset drivers, download updates from your computer maker's support page or from the graphics card maker's site.

Outdated drivers can cause freezes and slow performance.

## Fix 7: Repair damaged system files

Corrupted Windows files can cause slowness and strange errors.

1. Click Start, type `cmd`, right-click **Command Prompt**, and choose **Run as administrator**.
2. Run:

```
sfc /scannow
```

3. When it finishes, run:

```
DISM /Online /Cleanup-Image /RestoreHealth
```

4. Restart the computer.

Each command can take several minutes. Let them finish without closing the window.

## If it is still slow: hardware upgrades

When software fixes are not enough, hardware is often the limit:

| Upgrade | When it helps |
| --- | --- |
| **SSD instead of a hard drive** | The biggest speed boost for an older PC that still has a mechanical hard drive. Boot and loading times drop sharply |
| **More RAM** | If Task Manager shows memory nearly full while you work (8 GB is a practical minimum today, 16 GB is more comfortable) |
| **Cleaning dust and fans** | If the PC gets hot and the fans are loud, which can slow the processor down to protect it |

Before buying anything, check your model's specifications to make sure the upgrade is compatible.

## Last resort: reset Windows

If nothing helps, **Settings > System > Recovery > Reset this PC** reinstalls Windows. Back up your files first. Choose the option to keep your files if you want to avoid losing documents, but note you will need to reinstall your programs.

## Prevention tips

- Install only the programs you need
- Restart weekly
- Keep at least 15 percent of the drive free
- Keep Windows and your security software updated
- Be careful with free software bundles and browser extensions

If your PC will not show anything on the screen at all, see [PC Turns On but No Display? 5 Fixes](pc-turns-on-no-display.html). For a specific slowdown you cannot solve, send me the details on the [Contact page](../contact.html).
