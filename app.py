from flask import Flask, render_template, request, url_for
from time import strftime
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html", date=strftime("%Y-%m-%d"))

@app.route('/graph', methods=['POST'] )
def graph():
    date = request.form["date"]
    start_time = request.form["start_time"]
    print(start_time)
    duration_sec = int(request.form["duration_min"]) * 60   # * 15 min * 60 sec/min
    #import graph.py
    url_for('static', filename='graph.png')
    return render_template("index.html", date=date,  start_time=start_time, duration_sec=duration_sec)
    