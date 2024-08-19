import api_request as api

"""
klasa lokalizacja przetrzymuje aktualnie wyszukiwane miasto - nazwa, id
id jest pobierane z api podczas inicjalizacji obiektu
klasa przyjmuje dwa parametry - domyslnie wymagany jest jeden drugi wykorzystujemy jezeli pobieramy dane z pliku
"""
class Location:
    def __init__(self, city, id = 0):
        self.city = city
        if id == 0:
            self.id = api.request_for_id(city)
        
        else: 
            self.id = id

        if self.id != 0:
            self.save_log()

    def __str__(self):
        return f"Miasto: {self.city}, posiada id: {self.id}"

    def get_id(self):
        return self.id

    """
    save_log()
    funkcja po zainicjalizowaniu zapisuje do pliku dane potrzebne do automatycznego wyszukania po ponowym uruchomieniu aplikacji
    """

    def save_log(self):
        with open('city.csv', "w") as file:
            file.write(f"{self.city},{self.id}")
        file.close()