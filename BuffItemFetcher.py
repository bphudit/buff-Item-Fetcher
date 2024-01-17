import requests
import re

class BuffItemFetcher:
    def __init__(self):
        self.item_data = self.get_buff_item_data()
        self.phase_check = {
            'Phase 1': 'P1',
            'Phase 2': 'P2',
            'Phase 3': 'P3',
            'Phase 4': 'P4',
            'Emerald': 'Emerald',
            'Saphhire': 'Sapphire',
            'Black Pearl': 'Black Pearl'
        }
        self.item_price_cache = {}
        self.item_liquidity_cache = {}

    def item_name_to_buffid(self, item_name):
        # Try to find the phase in the item name
        phase_match = re.search(r"(Phase \d+|Emerald|Sapphire)$", item_name)
        
        if phase_match:
            # If phase is found in the item name, extract it and the item name
            item_name_without_phase = item_name[:phase_match.start() - 3]
            phase = self.phase_check[phase_match.group()]
        else:
            # If no phase is found, use the entire item name
            item_name_without_phase = item_name
            phase = None

        item_id = self.item_data.get(item_name_without_phase)

        return item_id, phase
    
    def get_buff_price(self, item_name):
        item_id, phase = self.item_name_to_buffid(item_name)

        if not item_id:
            return None  # Handle the case where item_id is not found

        # Check if the item price is already in the cache
        if item_id in self.item_price_cache:
            return self.item_price_cache[item_id], self.item_liquidity_cache[item_id]

        url = "https://buff.163.com/api/market/goods/sell_order"
        payload = {
            'game': 'csgo',
            'goods_id': item_id,
            'page_num': 1
        }
        headers = {
            'Accept-Language': 'en-US,en;q=0.9',
        }

        
        response = requests.get(url, headers=headers, params=payload)
        
        items = response.json()['data']['items']

        if phase:
            # Filter items by phase if phase was found
            for item in items:
                item_phase = item['asset_info']['info']['phase_data']['name']
                if  item_phase == phase:
                    price = float(item['price'])
                    break
            else:
                return None  # Handle the case where the specific phase item is not found
        else:
            price = float(items[0]['price'])

        liquid = response.json()['data']['total_count']

        # Cache the item price for future use
        self.item_price_cache[item_id] = price
        self.item_liquidity_cache[item_id] = liquid

        return price, liquid


    def get_buff_item_data(self):
        item_data = {}
        with open(r'buffids.txt', 'r', encoding='utf-8') as file:
            for line in file:
                parts = line.strip().split(';')
                if len(parts) == 2:
                    item_id, item_name = parts
                    item_data[item_name.strip()] = item_id
        return item_data
    
    def reset_cache(self):
        self.item_price_cache = {}
        self.item_liquidity_cache = {}


def main():
    pass

if __name__ == "__main__":
    main()
