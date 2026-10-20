---
title: LAN Connected but No Internet? Step-by-Step Troubleshooting
description: Your computer shows it is connected to the network but websites will not open. Follow these steps to find whether the problem is the PC, router, DNS or provider.
category: networking
date: 2026-10-15
---

The network icon says you are connected, but websites will not load. This usually means your computer is talking to the router, but the router (or something after it) is not passing traffic to the internet.

The fastest way to fix it is to find **where** the break is. This guide helps you do that in a few minutes.

## Step 1: Find out how big the problem is

Ask yourself:

- Do other devices (phones, other PCs) have internet on the same network?
- Does it fail on every website or only some?
- Did it stop suddenly, or after a Windows update, a power cut or a router change?

| Result | Likely cause |
| --- | --- |
| Only one computer has no internet | Problem is on that computer (settings, adapter, driver) |
| All devices have no internet | Router, modem or the internet provider |
| Some sites work, some do not | DNS problem |

## Step 2: Restart the modem and router

Many problems end here.

1. Unplug the power from the modem and the router.
2. Wait 30 seconds.
3. Plug in the modem first and wait until its lights settle, then plug in the router.
4. Wait two minutes and test again.

## Step 3: Check cables and lights

- Make sure the network cable clicks firmly into both the computer and the router
- Look at the lights on the network port. A light that is off can point to a bad cable or port
- Try a **different cable** and a **different port on the router**
- Check the cable running into the modem is not loose

## Step 4: Run the Windows network troubleshooter

1. Open **Settings > Network & Internet**.
2. Choose **Network troubleshooter** (or **Advanced network settings > Network reset** later if needed).
3. Follow the steps and read the result it gives.

## Step 5: Release and renew the IP address

1. Click Start, type `cmd`, right-click **Command Prompt**, and choose **Run as administrator**.
2. Type these commands, pressing Enter after each one:

```
ipconfig /release
ipconfig /renew
ipconfig /flushdns
```

3. Test the internet again.

## Step 6: Check what IP address you received

In the same Command Prompt window, type:

```
ipconfig
```

Look at **IPv4 Address**:

- If it starts with **169.254**, your computer did not get an address from the router. Check the cable and router, and make sure DHCP is turned on in the router settings.
- If it looks like **192.168.x.x** or **10.x.x.x**, you have a normal address, so continue.

## Step 7: Find where the connection stops using ping

Type these commands one at a time:

1. `ping 192.168.1.1` (use your router's address, shown as **Default Gateway** in `ipconfig`)
2. `ping 8.8.8.8`
3. `ping google.com`

| What happens | Meaning |
| --- | --- |
| First ping fails | Problem between your PC and the router (cable, adapter, IP settings) |
| First works, second fails | Router has no internet (modem, provider) |
| Second works, third fails | **DNS problem** |

## Step 8: Fix a DNS problem

If `ping 8.8.8.8` works but `ping google.com` fails, change your DNS servers:

1. Open **Control Panel > Network and Sharing Center > Change adapter settings**.
2. Right-click your connection and choose **Properties**.
3. Double-click **Internet Protocol Version 4 (TCP/IPv4)**.
4. Choose **Use the following DNS server addresses** and enter `8.8.8.8` and `8.8.4.4` (or `1.1.1.1` and `1.0.0.1`).
5. Click OK and test.

## Step 9: Reset the network stack

If nothing worked, reset the network settings. In an administrator Command Prompt:

```
netsh winsock reset
netsh int ip reset
```

Restart the computer afterwards.

## Step 10: Check proxy, VPN and security software

- Turn off any **VPN** and test
- Open **Settings > Network & Internet > Proxy** and make sure no proxy is turned on unless you use one
- Temporarily test with your firewall or third-party security program paused (turn it back on right after)

## Step 11: Contact your internet provider

If every device is offline, the modem lights show a problem, and a restart did not help, call your provider. Tell them which steps you have already tried and which lights are on or off. It will save time.

## Prevention tips

- Use good-quality network cables
- Restart the router every few weeks if it is old
- Keep Windows and network drivers updated
- Avoid manual IP addresses unless needed, to prevent conflicts

Need help with a specific error? Send the details on the [Contact page](../contact.html).
