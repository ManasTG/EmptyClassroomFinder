# Empty Classroom Finder

This project dynamically scrapes of Timetable data from the IILM Uni, GN website and then calculate which classes are empty that the user selected the period and day for.

### Why was it needed?
There is already a project which does essentially the same thing but, it has one problem: the site owner has to manually update the timetable if the university made some changes to the timetable. Inturn, making the site unreliable if not updated.


This project solves that problem by scraping the timetable directly from the university's website.

A Github Action workflow runs where it trigger's the scraping process every morning 7AM. If the timetable has changed, the updated JSON data is committed to the repository. If there are no changes, no commit is made.

## Features

- Automatically scrapes the latest timetable data
- Automatically updates timetable data when changes are detected
- Calculates which classrooms are empty for a selected day and period
- Provides a simple web interface for finding empty classrooms


## Tech

Following were the tech needed for created the project:

- Python
- Flask API
- JSON for storing timetable data
- Selenium for web scraping
- Vanilla JavaScript
- HTML/CSS
- GitHub Actions for automation

## Architecture

Scrapes from IILM website -> JSON file -> Use Python for Logic -> Simple Frontend to show the empty classroom
#### Process
<img width="677" height="962" alt="Process" src="https://github.com/user-attachments/assets/368d7a7f-3f68-4b56-bca6-82beb12bb57d" />

#### Workflow Simplifies
<img width="496" height="207" alt="WorkflowSimplified" src="https://github.com/user-attachments/assets/30e35681-352b-4e5b-9e97-af594e4a925b" />



## File Struture

```
├── app.py
├── frontend
│   ├── index.html
│   ├── script.js
│   └── style.css
├── README.md
├── requirements.txt
├── scraper
│   ├── generalScraper.py
│   └── scraper.py
├── src
│   ├── allClassroom.json
│   ├── allClassroom.py
│   ├── emptyClassroom.py
│   └── testing.py
└── timetable.json
```

## Deployment

The site was deployed on `Render` but was routed through `Cloudflare`.

## Future Additions

- Making the frontend Prettier
- Move database from `.json` to structred database (eg. Postgresql)

## Credits

### Made by
*Manas*

### Supporters
- Rakesh Kumar Sharma
- Devashish Srivastava
- Md Asif
- Md Imran Ansari
- Raj Gupta

### Inspired from

['Find an Empty Classroom' by Sakshi K](https://iilm-vacant-classroom-finder.onrender.com/)
