import requests
from requests.models import Response
parameters = {
    "lat" : 45.0,
    "lon" : -122.3
}

response = requests.get("http://api.open-notify.org/iss-now.json",params= parameters)
#print(response.status_code())
print(response.json())