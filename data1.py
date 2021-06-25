import plotly.express as px
import pandas as pd
import csv
import numpy as np

with open('Student Marks vs Days Present.csv', encoding = 'utf8') as a:
    df = pd.read_csv(a)
    fig = px.scatter(df, x = 'Marks In Percentage', y = 'Days Present', title='Student Marks vs Days Present')
    fig.show()

def getDataSource(dataPath):
   marks = []
   days = []
   with open(dataPath) as a:
     d = csv.DictReader(a)
     for row in d:
       marks.append(float(row['Marks In Percentage']))
       days.append(float(row['Days Present']))
     return {'x':marks, 'y' : days}

def findCorrelation(dataSource):
  correlation = np.corrcoef(dataSource['x'], dataSource['y'])
  print(correlation[0,1])

def main():
  dataPath = 'Student Marks vs Days Present.csv'
  dataSource = getDataSource(dataPath)
  findCorrelation(dataSource)

main()