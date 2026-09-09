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

# Interaction with the classes drop-down menu
classes = driver.find_element("css selector",'span[title="Classes"]').click()

dropdown = driver.find_element("css selector", '[class ="dropDownPanel asc-context-menu"]')
sections = dropdown.find_elements("xpath", 'li/a')

# Loop and Store the name of the sections
sectionList = []
for section in sections:
    sectionList.append(section.text)

print(sectionList)


# Parsing
days = {
    0:"Monday",
    1:"Tuesday",
    2:"Wednesday",
    3:"Thursday",
    4:"Friday",
    5:"Saturday"
}


for i in range(len(sectionList)):
    classes = driver.find_element("css selector",'span[title="Classes"]').click()
    dropdown = driver.find_element("css selector", '[class ="dropDownPanel asc-context-menu"]')
    section = dropdown.find_element("xpath", f'//a[text()="{sectionList[i]}"]')

    section.click()

    time.sleep(0.1)

    print("================")
    print(sectionList[i])
    print("================")

    rects = driver.find_elements(
    "css selector",
    'rect[fill="transparent"]'
    )

    for rect in rects:
        title = rect.find_elements("tag name", "title")

        x = int(rect.get_attribute("x"))
        y = int(rect.get_attribute("y"))

        period = (x - 345)/285
        day = (y - 420)/255

        if not title:
            continue

        print("--------------------")
        print("Period:", int(period+1))
        print("Day:", days[day])
        print("TITLE:")
        print(title[0].get_attribute("textContent"))

driver.quit()
