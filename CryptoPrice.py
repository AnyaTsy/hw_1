import requests
from colorama import Fore, Style

T = Fore.RED
RES = Style.RESET_ALL

class CryptoPriceFetcher:
    def __init__(self, crypto_names=None):
        if crypto_names is None:
            crypto_names = ['bitcoin', 'ethereum', 'ripple', 'monero']
        self.crypto_names = crypto_names

    def get_crypto_prices(self):
        api_url = 'https://api.coingecko.com/api/v3/simple/price'
        params = {
            'ids': ','.join(self.crypto_names),
            'vs_currencies': 'usd',
        }

        try:
            response = requests.get(api_url, params=params)
            data = response.json()
            if response.status_code == 200:
                prices = {name.capitalize(): data[name]['usd'] for name in self.crypto_names}
                return prices
            else:
                print(f"{T}Error: Unable to fetch crypto prices (Status Code: {response.status_code}){RES}")
        except Exception as e:
            print(f"{T}An error occurred: {str(e)}{RES}")

    def display_crypto_prices(self):
        crypto_prices = self.get_crypto_prices()
        if crypto_prices:
            print(f"{Fore.GREEN}Crypto Prices (USD):{RES}")
            for name, price in crypto_prices.items():
                print(f"{Fore.CYAN}{name}:{Fore.YELLOW} ${price:.2f}{RES}")
        else:
            print(f"{T}Failed to fetch crypto prices.{RES}")


if __name__ == "__main__":
    crypto_price_fetcher = CryptoPriceFetcher()
    crypto_price_fetcher.display_crypto_prices()


