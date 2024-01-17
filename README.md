# BuffItemFetcher for Game Marketplace

## Overview
`BuffItemFetcher` is a Python utility for fetching and analyzing item data from an online game marketplace. It is designed to retrieve item prices and liquidity details, focusing on items with specific attributes like phases or special features.

## Features
- Fetches item data based on name and attributes (e.g., phases like 'Phase 1', 'Emerald').
- Caches prices and liquidity information to optimize performance.

## Prerequisites
- Python 3.x
- `requests` library
- `re` (regular expressions) module

## Installation
1. Ensure Python 3.x is installed.
2. Install `requests` library: `pip install requests`
3. Place the `buffids.txt` file with item names and IDs in the script's directory.

## Usage
- Initialize the class: `fetcher = BuffItemFetcher()`
- Fetch item data: `price, liquidity = fetcher.get_buff_price(item_name)`
- The script supports fetching prices for items with or without specified phases.

