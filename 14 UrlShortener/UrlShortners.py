from pyshorteners import Shortener

ACCESS_TOKEN = "2eb046a4273e51a1837cc50a96b9501e20decc72"

long_url = input()
url_shortener = Shortener(domain="bit.ly", api_key=ACCESS_TOKEN)
print("Short URL is : ", format(url_shortener.bitly.short(long_url)))
