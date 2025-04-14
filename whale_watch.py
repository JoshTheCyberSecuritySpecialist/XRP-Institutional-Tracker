import requests

def check_account_balance(account):
    url = "https://s2.ripple.com:51234/"
    headers = {"Content-Type": "application/json"}
    payload = {
        "method": "account_info",
        "params": [{
            "account": account,
            "ledger_index": "validated"
        }]
    }
    response = requests.post(url, json=payload, headers=headers)
    data = response.json()
    balance = int(data['result']['account_data']['Balance']) / 1_000_000
    return balance
