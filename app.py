from flask import Flask, render_template, request, url_for
from datetime import datetime, timedelta
import subprocess, json
from graph import graphJson
app = Flask(__name__)

@app.route('/')
def index():
    today=datetime.now().strftime("%Y-%m-%d")
    hour_ago=(datetime.now() - timedelta(hours = 1) ).strftime("%H:%M")

    url_for('static', filename='style.css')
    return render_template("index.html", date=today, time=hour_ago, duration_min=30 )

@app.route('/graph', methods=['POST'] )
def graph():
    # Set parameters
    date_str = request.form["date"]
    time_str = request.form["start_time"]
    duration_min = int(request.form["duration_min"])
    
    # Calculate End time
    start_datetime_str = "T".join([date_str, time_str])
    start_datetime = datetime.strptime( start_datetime_str, "%Y-%m-%dT%H:%M" )
    end_datetime = start_datetime + timedelta(minutes=duration_min)
    end_datetime_str = end_datetime.strftime("%Y-%m-%dT%H:%M")

    # Filter data log and finish formatting into Json
    input_filepath = "pid.log"
    output_filepath = "/tmp/ArduinoOven_json"
    filterdate_outputjson_bash_script = ["bash", "logFilterDate.sh", start_datetime_str, end_datetime_str, input_filepath, output_filepath]
    subprocess.Popen(filterdate_outputjson_bash_script)

    # Parse data and Graph
    json_file = open(output_filepath,'r')
    readings = json.load(json_file)

    graphJson(readings)

    #import graph.py

    url_for('static', filename='graph.png')
    url_for('static', filename='style.css')
    return render_template("index.html", date=date_str, time=time_str, title=str(end_datetime), duration_min=duration_min)
