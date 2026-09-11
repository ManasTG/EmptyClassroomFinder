import json
import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

# Needs changing when deploying to the server
options = Options()
# options.binary_location = "/snap/firefox/current/usr/lib/firefox/firefox" # FOR TESTING
options.add_argument("--headless")  # FOR PRODUCTION

# Loads the browser and the uni site
driver = webdriver.Firefox(options=options)
driver.get("https://iilmgn.edupage.org/timetable/")

time.sleep(2)   # Wait for js/svg to load

# Faculty list; for checking ambiguity
faculty = driver.find_element("css selector", 'span[title="Teachers"]').click()
facultyDropdown = driver.find_element("css selector",'[class ="dropDownPanel asc-context-menu"]')
facultyNames = facultyDropdown.find_elements("xpath", 'li/a')

facutlyList = []
for facultyName in facultyNames:
    facutlyList.append(facultyName.text)

# print(facutlyList)

# Interaction with the classes drop-down menu
classes = driver.find_element("css selector",'span[title="Classes"]').click()

dropdown = driver.find_element("css selector", '[class ="dropDownPanel asc-context-menu"]')
sections = dropdown.find_elements("xpath", 'li/a')

# Loop and Store the name of the sections
# sectionList = ['1BCA1'] # FOR TESTING
sectionList = []  # FOR USE

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

allData = []

for i in range(len(sectionList)):
    classes = driver.find_element("css selector",'span[title="Classes"]').click()
    dropdown = driver.find_element("css selector", '[class ="dropDownPanel asc-context-menu"]')
    section = dropdown.find_element("xpath", f'//a[text()="{sectionList[i]}"]')

    section.click()

    time.sleep(0.1)

    print("============================")
    print("============================")
    print(sectionList[i])
    print("============================")
    print("============================")

    rects = driver.find_elements(
    "css selector",
    'rect[fill="transparent"]'
    )

    for rect in rects:
        title = rect.find_elements("tag name", "title")

        x = float(rect.get_attribute("x"))
        y = float(rect.get_attribute("y"))

        def labChecker():
            labCheck = float(rect.get_attribute("width"))

            if labCheck > 285:
                return[int(period+1), int(period+2)]

            else:
                return[int(period+1)]

        period = (x - 345)/285
        day = (y - 420)/255

        if not title:
            continue

        title = title[0].get_attribute("textContent")
        parts = title.split("\n")   # To split off the content in title (subject [0], faculty [1], classroom [2])
        #
        # classroom = parts[2].strip() if len(parts)==3 else parts[3].strip() # Check if there is lab or not
        if parts[-1].strip() in facutlyList:
            classroom = None
        else:
            classroom =  parts[-1].strip()

        subject = parts[0].strip()

        data = {
            "Section": sectionList[i],
            "Subject": subject,
            "Classroom": classroom,
            "Period": labChecker(),
            "Day": days[int(day)]
            }
        # print("--------------------")
        # print("Period:", labChecker())
        # print("Day:", days[int(day)])
        # print("Part:")
        # print(parts)
        # print("Classroom:", classroom)
        # print("TITLE:")
        # print(title) # [0].get_attribute("textContent"))

        allData.append(data)  # TURNED OFF FOR TESTING

        # print(data)   # TURNED OFF FOR TESTING


with open("test.json", "w", encoding="utf-8") as f:  # TURNED OFF FOR TESTING
    json.dump(allData, f, indent=4, ensure_ascii=False)

driver.quit()
