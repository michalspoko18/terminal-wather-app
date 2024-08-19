import api_request as api
import forecast as function
import weather 
import helpers
from icecream import ic
import os
import csv
import sys

start_flag = 0

def main():
    global start_flag

    location_forecast = {}

    """
    jezeli istnieje plik i nie jest pusty to dane miasto zostanie wyszukane z pliku
    """
    if start_flag == 0 and os.path.exists("city.csv") and os.path.getsize("city.csv") != 0:
        #ic("TEST")
        with open('city.csv') as file:
            reader = csv.reader(file, delimiter=',')
            data  = list(reader)
        location_forecast[data[0][0]] = weather.Location(data[0][0], data[0][1])
        city = data[0][0]
        if data[0][1] == 0:
            id = location_forecast[city].get_id()
        else: id = data[0][1]
        start_flag = 1

        """
        jezeli pliku nie ma to poprosi usera o wprowadzenie nazwy miasta i przeprowadzi walidacje
        """
    
    else:
        city = str(input("Podaj miasto: "))

        while helpers.input_valid(city) is False:
            city = input("Podaj miasto (0 - wyjscie): ")
        if city == '0': sys.exit()

        location_forecast[city] = weather.Location(city)
        id = location_forecast[city].get_id()

    
    forecast = []
    
    forecast = function.getForecast(id)
    """
    przy kazdym wyszukaniu konsola bedzie czyszczona i zostana wyswietlone informacje o danej lokalizacji oraz mozliwosc wyszukania kolejnej lub wyjscia
    """
    if forecast != 0:
        os.system('clear')
        weather_now = forecast[0]
        weather_future = forecast[1]

        br = ""

        print(f"\nPogoda dla: {city}")
        print(br.center(10, "-"))

        print("\nAktualna pogoda:")
        print(f" - Temperatura: {weather_now[2]}\u00b0C \n - Odczuwalna temperatura: {weather_now[3]}\u00b0C \n - Prędkość wiatru: {weather_now[4]} km/h \n - Opady deszczu: {weather_now[5]} mm \n - Opady śniegu: {weather_now[6]} cm \n")
        print(f"Dodatkowe informacje:\n - Opis: {weather_now[1]} \n - Ikona: {weather_now[0]}.png")

        print("\nPogoda 4 dniowa:")

        for x in range(1,5):
            print(f" - {weather_future[x][0][:10]} Temeratura minimalna: {weather_future[x][1]} Temperatura maksymalna: {weather_future[x][2]}")

        print(br.center(10,"-"))

if __name__ == "__main__":
    
    while True:
        main()  