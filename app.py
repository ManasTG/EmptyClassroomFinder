import os
import psycopg2
from flask import Flask, jsonify, request, send_from_directory
from src.emptyClassroom import emptyClassroomFinder

app = Flask(__name__, static_folder="frontend", static_url_path="")

def init_db():
    conn = psycopg2.connect(os.environ["DATABASE_URL"])
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS timetable (
            id SERIAL PRIMARY KEY,
            section TEXT NOT NULL,
            classroom TEXT,
            day TEXT NOT NULL,
            period INTEGER NOT NULL
        )
    """)

    conn.commit()
    cur.close()
    conn.close()

@app.before_request
def log_request():
    print(f"Incoming requests: {request.method} {request.url}")

@app.after_request
def log_response(response):
    print(f"Outgoing requests: {response.status_code}")
    return response

@app.route('/emptyClassroomFinder')
def home():
    return send_from_directory('frontend', 'index.html')

@app.route('/find')
def find_room():
    day = request.args.get("day")
    period = request.args.get("period")

    rooms = emptyClassroomFinder([int(period)], day)

    return jsonify(rooms)


init_db()

if __name__ == "__main__":
    app.run()

