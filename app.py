from flask import Flask, jsonify, request, send_from_directory
from src.emptyClassroom import emptyClassroomFinder

app = Flask(__name__, static_folder="frontend", static_url_path="")

@app.before_request
def log_request():
    print(f"Incoming requests: {request.method} {request.url}")

@app.after_request
def log_response(response):
    print(f"Outgoing requests: {response.status_code}")
    return response

@app.route('/')
def home():
    return send_from_directory('frontend', 'index.html')


@app.route('/find')
def find_room():
    day = request.args.get("day")
    period = request.args.get("period")

    rooms = emptyClassroomFinder([int(period)], day)

    return jsonify(rooms)

if __name__ == "__main__":
    app.run()
