from flask import Flask, render_template, request, url_for
from datetime import datetime, timedelta
app = Flask(__name__)

@app.route('/')
def index():
    today=datetime.now().strftime("%Y-%m-%d")
    hour_ago=(datetime.now() - timedelta(hours = 1) ).strftime("%H:%M")

    url_for('static', filename='style.css')
    return render_template("index.html", date=today, time=hour_ago, duration_min=30 )

@app.route('/graph', methods=['POST'] )
def graph():
    date_str = request.form["date"]
    time_str = request.form["start_time"]
    duration_min = int(request.form["duration_min"])
    
    start_datetime_str = " ".join([date_str, time_str])
    start_datetime = datetime.strptime( start_datetime_str, "%Y-%m-%d %H:%M" )
    end_datetime = start_datetime + timedelta(minutes=duration_min)
    #import graph.py

    url_for('static', filename='graph.png')
    url_for('static', filename='style.css')
    return render_template("index.html", date=date_str, time=time_str, title=str(end_datetime), duration_min=duration_min)
