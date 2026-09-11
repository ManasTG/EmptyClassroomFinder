import json

f = open("/run/media/krane/Local Disk 2/Projects/OpenSource/emptyClassroom/EmptyClassroomFinder/src/allClassroom.json", "r")

d = open("/run/media/krane/Local Disk 2/Projects/OpenSource/emptyClassroom/EmptyClassroomFinder/test.json", "r")

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


