import plotly.express as px
import pandas as pd
import csv
import numpy as np

with open('cups of coffee vs hours of sleep.csv') as a:
    df = pd.read_csv(a)
    fig = px.scatter(df, x = 'Coffee in ml', y = 'sleep in hours', title='cups of coffee vs hours of sleep')
    fig.show()


def getDataSource(dataPath):
   coffee = []
   sleep = []
   with open(dataPath) as a:
     d = csv.DictReader(a)
     for row in d:
       coffee.append(float(row['Coffee in ml']))
       sleep.append(float(row['sleep in hours']))
     return {'x': coffee, 'y' : sleep}

def findCorrelation(dataSource):
  correlation = np.corrcoef(dataSource['x'], dataSource['y'])
  print(correlation[0,1])

def main():
  dataPath = 'cups of coffee vs hours of sleep.csv'
  dataSource = getDataSource(dataPath)
  findCorrelation(dataSource)

main()