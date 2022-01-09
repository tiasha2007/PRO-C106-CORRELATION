import csv
import numpy as np

def getDataSource(data_path):
    Coffee_in_ml=[]
    sleep_in_hours=[]
    with open(data_path) as csv_file:
        csv_reader=csv.DictReader(csv_file)
        for row in csv_reader:
            Coffee_in_ml.append(float(row["Coffee in ml"]))
            sleep_in_hours.append(float(row["sleep in hours"]))
        
    return {"X":sleep_in_hours, "Y":Coffee_in_ml}

def findCorrelation(datasource):
    correlation=np.corrcoef(datasource["X"],datasource["Y"])
    print("correlation between cups of coffee vs hrs of sleep: \n--->",correlation[0,1])

def setup():
    data_path="cups_of_coffee_vs_hrs_of_sleep.csv"
    datasource=getDataSource(data_path)
    findCorrelation(datasource)

setup()
