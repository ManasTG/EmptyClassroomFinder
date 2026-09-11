# Empty Classroom Finder

## Tech

For creating empty classroom from timetable Fetched from IILM University GN website. 

- Python
- FastFetch
- SQLite

## Architecture

Scrapes from IILM website -> JSON file -> Use Python for Logic -> Simple Frontend to show the empty classroom

Local Workflow: scraper.py -> allClassroom.py -> emptyClassroom.py

## roadmap
1. Built a scraper that works for one page.(8/9/26)
2. work on extracting the exact period and day of that lecture using x,y ht,wt
3. work on the edge cases for labs-> changes with float
4. the main empty classroom logic works
5. took care of some none classroom edge cases
6. work on the console version of empty room finder
7. work on simple js fronted
