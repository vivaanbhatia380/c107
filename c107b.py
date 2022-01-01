import pandas as pd
import csv
import plotly.graph_objects as go 

df=pd.read_csv('c107.csv')
studentdf=df.loc[df['student_id']=='TRL_imb']
mean=studentdf.groupby('level')['attempt'].mean()
fig=go.Figure(go.Bar(
    x=mean,y=['level1','level2','level3','level4'],
    orientation ='h'
))
fig.show()