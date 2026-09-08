import requests
from bs4 import BeautifulSoup as bs

res = requests.get('https://iilmgn.edupage.org/timetable/')
print(res.status_code)
print(res.content)

F# etch and parse the page
soup = bs(res.content, 'html.parser')

print(soup.prettify())
