from flask_googlemaps import get_address, get_coordinates
import requests as rq

API_KEY = 'AIzaSyBy-w4jKXwXyvC2uCXzin766QcunNCbkQQ'
API_KEY2 = 'AIzaSyCOGR1fl_niKbOEPI-oVhiBmGm8no02A80'


def get_coordinates(API_KEY, address_text):
    response = rq.get(
        "https://maps.googleapis.com/maps/api/geocode/json?address="
        + address_text
        + "&key="
        + API_KEY
    ).json()
    
    print("message de response",response)
    return response["results"][0]["geometry"]["location"]

# get_coordinates(API_KEY,'dakar')
print(get_coordinates(API_KEY2,'Netaji Subhash Engineering College Kolkata'))
