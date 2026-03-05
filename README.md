# TERMUX TEAM PROXY CHECKER TOOL

A simple and fast **Proxy Scraper & Checker** tool for Termux written in Python.

This tool allows users to scrape free proxies from multiple online sources and check whether they are **LIVE or DEAD**.

## Features

- 🔹 **Proxy Scraper**
  - Collects fresh proxies from multiple GitHub proxy sources.
  - Automatically saves them into `proxies.txt`.

- 🔹 **Proxy Checker**
  - Checks proxies using multi-threading.
  - Detects **LIVE** and **DEAD** proxies.

- 🔹 **Auto Result Save**
  - Working proxies are automatically saved into `live.txt`.

- 🔹 **Fast Checking**
  - Uses ThreadPoolExecutor for faster proxy checking.

## Installation

```bash
pkg update && pkg upgrade
pkg install python git
git clone https://github.com/termuxteam-cyber/proxy-tool.git
cd <proxy-tool>
python proxy_checker.py