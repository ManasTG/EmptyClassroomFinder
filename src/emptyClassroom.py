import json

f = open("allClassroom.json", "r")

d = open("../test.json", "r")

allClassroom = set(json.load(f))
timetable = json.load(d)
emptyClassroom = []


def emptyClassroomFinder(localPeriod, localDay):
    occupiedClassroom = set()

    for item in timetable:
        if item["Day"]==localDay and localPeriod[0] in item["Period"]:
            occupiedClassroom.add(item["Classroom"])

    emptyClassroom = allClassroom - occupiedClassroom

    return sorted(emptyClassroom)


