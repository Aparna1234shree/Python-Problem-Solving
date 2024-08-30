import requests

class CountryData:
    def __init__(self, url):
        self.url = url
        self.data = None

    def fetch_data(self):
        try:
            response = requests.get(self.url)
            response.raise_for_status()
            self.data = response.json()
        except requests.RequestException as e:
            print(f"Error fetching data: {e}")

    def display_countries_currencies(self):
        if self.data:
            for country in self.data:
                name = country.get('name', {}).get('common', 'Unknown')
                currencies = country.get('currencies', {})
                for currency, details in currencies.items():
                    symbol = details.get('symbol', 'No symbol')
                    print(f"Country: {name}, Currency: {currency}, Symbol: {symbol}")
        else:
            print("No data available. Please fetch data first.")

    def countries_with_currency(self, currency_name):
        if self.data:
            countries = []
            for country in self.data:
                currencies = country.get('currencies', {})
                for currency, details in currencies.items():
                    if currency_name in currency:
                        countries.append(country.get('name', {}).get('common', 'Unknown'))
                        break
            return countries
        else:
            print("No data available. Please fetch data first.")
            return []

# Usage example
url = 'https://restcountries.com/v3.1/all'
country_data = CountryData(url)
country_data.fetch_data()
country_data.display_countries_currencies()
print("\nCountries with DOLLAR as currency:")
print(country_data.countries_with_currency('dollar'))
print("\nCountries with EURO as currency:")
print(country_data.countries_with_currency('euro'))
