import requests
from icecream import ic
import weather
import sys

API_KEY = ""

"""
request_for_id(wyszukiwane miasto)
funkcja wykonuje zapytanie do api accuweather, jezeli istnieje takie miasto zwracany jest jego id - potrzebny do dalszych zapytan  
"""
def request_for_id(location):
    url_id_location = f'http://dataservice.accuweather.com/locations/v1/cities/search?apikey={API_KEY}&q={location}&language=pl-pl'

    try:
        response = requests.post(url_id_location)
        if len(response.json()) == 0:
            ic("Brak lokalizacji")
            return 0

        else:
            location_id = response.json()[0].get('Key')
            response.raise_for_status()
            return location_id
    except requests.RequestException as err:
        print(f'Wystąpił błąd podczas zapytania: {err}')

"""
request_for_1_hour_forecast(id - miasta)
zapytanie zwraca spora paczek wiadomosci, my pobieramy pare przykladowych wartosci ktore sa najbardziej istotne 
ikona miala byc wykorzystywana w GUI
"""
def request_for_1hour_forecast(id):
    url_forecast = f'http://dataservice.accuweather.com/forecasts/v1/hourly/1hour/{id}?apikey={API_KEY}&language=pl-pl&details=true&metric=true'

    try:
        response = requests.post(url_forecast)

        #ic(response.json())

        """if response.json().get('Code') == "Unauthorized":
            ic("API request")
            sys.exit()"""

        response_details = response.json()[0]

        weather_now_info = []

        weather_now_info.append(response_details.get('WeatherIcon'))
        weather_now_info.append(response_details.get('IconPhrase'))
        weather_now_info.append(response_details.get('Temperature').get('Value'))
        weather_now_info.append(response_details.get('RealFeelTemperature').get('Value'))
        weather_now_info.append(response_details.get('Wind').get('Speed').get('Value'))
        weather_now_info.append(response_details.get('Rain').get('Value'))
        weather_now_info.append(response_details.get('Snow').get('Value'))


        return weather_now_info
    
    except requests.RequestException as err:
        print(f'Wystąpił błąd podczas wysyłania zapytania: {err}')


"""
request_for_5day_forecast(id - miasta)
zapytanie podobnie jak wyzsze zwraca sporo informacji, wybralismy najwazniejsze
prosta budowa json daj mozliwosc zautomatyzowania wyciagania informacji w danym standardzie jak dla konkretnych nastepnych dni dzieki petli for
"""
def request_for_5day_forecast(id):
    url_forecast = f'http://dataservice.accuweather.com/forecasts/v1/daily/5day/{id}?apikey={API_KEY}&language=pl-pl&metric=true'

    try:
        response = requests.post(url_forecast)
        
        response_details = response.json()

        weather_future_info = []

        day_details = []

        #weather_future_info.append(response_details.get('Headline').get('Text'))

        for x in range(5):
            day_details.append(response_details.get('DailyForecasts')[x].get('Date'))
            day_details.append(response_details.get('DailyForecasts')[x].get('Temperature').get('Minimum').get('Value'))
            day_details.append(response_details.get('DailyForecasts')[x].get('Temperature').get('Maximum').get('Value'))

            weather_future_info.append(day_details)
            day_details = []

        return weather_future_info
    except requests.RequestException as err:
        print(f'Wystąpił błąd podczas wysyłania zapytania: {err}')


