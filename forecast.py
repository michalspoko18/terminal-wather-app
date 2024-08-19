import api_request as api

"""
getForecast(id - miasta)
funkcja nadrzedna do pobierajacych prognoze pogody oraz agregujaca dane w jedna liste
"""
def getForecast(location_id):    
        
        if location_id != 0:
            
            data = []

            data.append(api.request_for_1hour_forecast(location_id))
            data.append(api.request_for_5day_forecast(location_id))

            return data

        else: 
            print("Wystąpił błąd spróbuj ponownie!") 
            return 0
