import requests
from bs4 import BeautifulSoup

URL = "https://sfbay.craigslist.org/d/artists/search/ats"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id="search-results")
result_element = results.find_all("li", class_="result-row")
for result in result_element:
    title = result.find("h3", class_="result-heading")
    print(title.text.strip())
