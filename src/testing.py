## To check if the timetable output matches or not
import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

f = open(BASE_DIR / "allClassroom.json", "r")
d = open(BASE_DIR.parent / "timetable.json", "r")

allClassroom = set(json.load(f))
timetable = json.load(d)

occupiedClassroom = set()
section = set()
classroomSection = []
emptyClassroom = set()

localPeriod = [5]
localDay = "Wednesday"

lengthAll = len(allClassroom)

for item in timetable:
    if item["Day"]==localDay and localPeriod[0] in item["Period"]:
        occupiedClassroom.add(item["Classroom"])
        section.add(item["Section"])

        classroomSection.append({
            "Section": item["Section"],
            "Classroom": item["Classroom"]
        })



for item in classroomSection:
    print(item)

print("All classroom:", lengthAll)
print("occupied:", len(occupiedClassroom))
print(f"free: {len(allClassroom) - len(occupiedClassroom)}")
# print(f"freeClassroom {allClassroom - occupiedClassroom}")
