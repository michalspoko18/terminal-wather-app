import api_request
from icecream import ic

"""
input_valid(wyszukiwane miasto)
funkcja walidujaca dane wejsiowe 
"""
def input_valid(value):
    #wyjatek dla wyjscia z programu
    if len(value) == 1 and value == '0':
        return True

    if not value:
        ic("not value")
        return False
    
    if any(char == " " for char in value):
        ic("space")
        return False

    if any(char.isdigit() for char in value):
        ic("digit")
        return False
    
    #sprawdza po odpowiedzi api czy wartosc jest id czy jest 0 - 0 oznacza bledna nazwe miasta
    if api_request.request_for_id(value) == 0:
        ic("api")
        return False

    return True