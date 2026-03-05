# TERMUX TEAM PROXY CHECKER TOOL

A professional **Proxy Scraper & Checker** tool for Termux.  
Easily scrape, check, and organize HTTP, HTTPS, SOCKS4, and SOCKS5 proxies.

## Features

- 🔹 **Proxy Scraper**: Grab fresh proxies from multiple online sources.
- 🔹 **Proxy Checker**: Test live/dead status for HTTP, HTTPS, SOCKS4, and SOCKS5 proxies.
- 🔹 **Speed Checker**: Measure latency of proxies.
- 🔹 **Country Checker**: Identify the country and ISP of a proxy.
- 🔹 **Port Scanner**: Scan open ports on a target IP.
- 🔹 **Live Proxy Display**: View all working proxies in real-time.
- 🔹 **Result Files**: Saves live proxies into `live.txt`, and can separate by type (`http.txt`, `https.txt`, `socks4.txt`, `socks5.txt`).

## Installation

```bash
pkg update && pkg upgrade
pkg install python git
git clone https://github.com/termuxteam-cyber/proxy-tool.git
cd <proxy-tool>
python proxy_checker.py