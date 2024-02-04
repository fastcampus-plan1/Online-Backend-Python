from anyio import sleep
import googlemaps

def geocode_address(address):
    gmaps = googlemaps.Client(key='AIzaSyBSlEhcoSjfSzvrHBl0BQUa20BqijmJQW0')
    geocode_result = gmaps.geocode(address)
    # sleep(1)
    return geocode_result
    # if geocode_result:
    #     location = geocode_result[0]['geometry']['location']
    #     latitude = location['lat']
    #     longitude = location['lng']
    #     return latitude, longitude
    # else:
    #     return None


print(geocode_address('서울특별시 강남구 역삼동 825-25'))