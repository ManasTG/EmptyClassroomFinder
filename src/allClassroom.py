import json

f = open("/run/media/krane/Local Disk 2/Projects/OpenSource/emptyClassroom/EmptyClassroomFinder/test.json", "r")

jsonData = json.load(f)

classroom = set()

for item in jsonData:
    if item["Classroom"] is not None:
        classroom.add(item["Classroom"])    # Extracts the value from Classroom and add it into the set

classroom = list(classroom)
# classroom = [c for c in classroom if c is not None]

classroom.sort()

print(classroom)

with open("allClassroom.json", "w") as f:
    json.dump(classroom, f)
