from pathlib import Path
import json

BASE_DIR = Path(__file__).resolve().parent

d = open(BASE_DIR.parent / "test.json", "r")

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
