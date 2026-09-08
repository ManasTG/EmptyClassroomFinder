import requests
import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

# Needs changing when deploying to the server
options = Options()
options.binary_location = "/snap/firefox/current/usr/lib/firefox/firefox"

# Loads the browser and the uni site
driver = webdriver.Firefox(options=options)
driver.get("https://iilmgn.edupage.org/timetable/")

time.sleep(2)   # Wait for js/svg to load

rects = driver.find_elements(
    "css selector",
    'rect[fill="transparent"]'
)

print("Found:", len(rects))

for rect in rects:
    title = rect.find_elements("tag name", "title")

    if not title:
        continue

    print("--------------------")
    print("x:", rect.get_attribute("x"))
    print("y:", rect.get_attribute("y"))
    print("width:", rect.get_attribute("width"))
    print("height:", rect.get_attribute("height"))
    print("TITLE:")
    print(title[0].get_attribute("textContent"))

# titles = driver.find_elements("tag name", "title")
#
# print("Titles:", len(titles))

driver.quit()
