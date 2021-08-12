#Import Dependencies
import datetime as dt
import numpy as np
import pandas as pd

#Import SQLAlchemy Dependencies and Flask D's
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify

#Create Engine
engine = create_engine("sqlite:///hawaii.sqlite")

#Set our base class
Base = automap_base()

#Reflect Database into our classes
Base.prepare(engine, reflect=True)

#Save our references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

#Start our Session
session = Session(engine)

#Define our flask app
app = Flask(__name__)

#Define "welcome" route or the root 
@app.route("/")

def welcome():
    return(
    '''
    Welcome to the Climate Analysis API!
    Available Routes:
    /api/v1.0/precipitation
    /api/v1.0/stations
    /api/v1.0/tobs
    /api/v1.0/temp/start/end
    ''')

#Precipitation Route
@app.route("/api/v1.0/precipitation")

def precipitation():
   prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
   #  .\ Below Signifies we want to continue the query in the next line
   precipitation = session.query(Measurement.date, Measurement.prcp).\
    filter(Measurement.date >= prev_year).all()
   precip = {date: prcp for date, prcp in precipitation}
   return jsonify(precip)

#Stations Route
@app.route("/api/v1.0/stations")

def stations():
    results = session.query(Station.station).all()
    # np.ravel() Unravels our results into a one dimensional array, then the list makes them into a list
    stations = list(np.ravel(results))
    #You do the stations= stations to format it into json
    return jsonify(stations=stations)

#Monthly Temperature Route
@app.route("/api/v1.0/tobs")

def temp_monthly():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    results = session.query(Measurement.tobs).\
      filter(Measurement.station == 'USC00519281').\
      filter(Measurement.date >= prev_year).all()
    temps = list(np.ravel(results))
    return jsonify(temps=temps)

#Max, Min, and Average Tempertature Route, Statistics Route
@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")

#Define stats and add a start and end parameter
def stats(start=None, end=None):
#Query our SQLite db, to get max, min, and avg., Call the list "sel"    
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]
# *sel in the query indicates there will be multiple results for the query
    if not end:
        results = session.query(*sel).\
            filter(Measurement.date >= start).all()
        temps = list(np.ravel(results))
        return jsonify(temps=temps) 

    results = session.query(*sel).\
        filter(Measurement.date >= start).\
        filter(Measurement.date <= end).all()
    temps = list(np.ravel(results))
    return jsonify(temps)