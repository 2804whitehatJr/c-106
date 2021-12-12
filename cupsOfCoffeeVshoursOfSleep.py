import csv
import numpy as np
import pandas as pd
import plotly.express as px

chart= pd.read_csv('cups of coffee vs hours of sleep.csv')

fig= px.scatter(chart,x='Coffee in ml',y='sleep in hours')
fig.show()

def getDataSource(data_path):
    cup_coffee = []
    hours_sleep = []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            cup_coffee.append(float(row["Coffee in ml"]))
            hours_sleep.append(float(row["sleep in hours"]))

    return {"x" : cup_coffee, "y": hours_sleep}

def findCorrelation(datasource):
    correlation = np.corrcoef(datasource["x"], datasource["y"])
    print("Correlation between Coffee in ml and sleep in hours :-  \n--->",correlation[0,1])

def setup():
    data_path  = "cups of coffee vs hours of sleep.csv"

    datasource = getDataSource(data_path)
    findCorrelation(datasource)

setup()