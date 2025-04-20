import requests
import json
from mamamdoor import keys
from access import KEYAPI

class ConvertionException(Exception):
    pass

class OldMoney:
    @staticmethod
    def convert(quote: str, base: str, amount: str):
        if quote == base:
            raise ConvertionException(f'Невозможно конвертировать одинаковое')

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ConvertionException(f'Не удалось обработать валюту {quote}')

        try:
            base_ticker = keys[base]
        except KeyError:
            raise ConvertionException(f'Не удалось обработать валюту {base}')

        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionException(f'Не удалось обработать количество {amount}')

        url = f"https://api.apilayer.com/exchangerates_data/convert?to={base_ticker}&from={quote_ticker}&amount={amount}"

        payload = {}
        headers = {
            "apikey": KEYAPI
        }

        response = requests.request("GET", url, headers=headers, data=payload)

        result = response.text
        result = json.loads(result)
        total_base = result['result']

        return total_base

