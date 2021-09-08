import plotly.express as pe
import csv
import pandas as pd 

df=pd.read_csv('data.csv')
student=df.loc[df['student_id']=='TRL_xsl']
print(student.groupby('level')['attempt'].mean())

graph=pe.bar(x=student.groupby('level')['attempt'].mean(),
            y=['level1','level2','level3','level4'],orientation='h')
graph.show()
