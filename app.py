from flask import Flask, render_template, jsonify
import csv

app = Flask(__name__)
filename = "pokertracker.csv"

# Read CSV and return rows as JSON
@app.route("/data")
def get_data():
    with open(filename) as f:
        reader = csv.DictReader(f)
        rows = list(reader)
    return jsonify(rows)

# Serve the main page
@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
