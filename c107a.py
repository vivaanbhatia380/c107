import csv
import pandas as pd
import plotly.graph_objects as go

df=pd.read_csv('c107.csv')
mean=df.groupby('level')['attempt'].mean()
print(mean)
fig=go.Figure(go.Bar(x=mean,y=['level1','level2','level3','level4'],orientation='h'))
fig.show()