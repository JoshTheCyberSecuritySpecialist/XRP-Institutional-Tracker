import requests

def get_xrp_volume():
    url = "https://api.coingecko.com/api/v3/coins/ripple"
    data = requests.get(url).json()
    volume = data['market_data']['total_volume']['usd']
    price = data['market_data']['current_price']['usd']
    return volume, price
