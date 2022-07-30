import requests
import json
from config import headers


class MoneyExchange:
    @staticmethod
    def get_price(base, quote, amount):
        url = f"https://api.apilayer.com/fixer/convert?to={quote}&from={base}&amount={amount}"
        response = requests.request('GET', url, headers=headers, data=None)
        response = json.loads(response.content)
        if not response['success']:
            return response['error']['info']
        else:
            result = response['result']
            return result

    @staticmethod
    def get_list():
        url = "https://api.apilayer.com/fixer/symbols"
        response = requests.request("GET", url, headers=headers, data=None)
        response = json.loads(response.content)['symbols']
        values = 'Available currencies:'
        for item in response:
            values = '\n'.join((values, f'{item} - {response[item]}'))
        return values


class APIException(Exception):
    pass
