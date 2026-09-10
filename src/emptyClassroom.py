import json

f = open("/run/media/krane/Local Disk 2/Projects/OpenSource/emptyClassroom/EmptyClassroomFinder/src/allClassroom.json", "r")

d = open("/run/media/krane/Local Disk 2/Projects/OpenSource/emptyClassroom/EmptyClassroomFinder/test.json", "r")

allClassroom = set(json.load(f))
timetable = json.load(d)
emptyClassroom = []
occupiedClassroom = set()

localPeriod = [4]
localDay = "Monday"

for item in timetable:
    if item["Day"]==localDay and localPeriod[0] in item["Period"]:
        occupiedClassroom.add(item["Classroom"])

# print(occupiedClassroom)
emptyClassroom = allClassroom - occupiedClassroom
print(emptyClassroom)

with open("emptyClassroom.json", "w") as f:
    json.dump(list(emptyClassroom), f)
