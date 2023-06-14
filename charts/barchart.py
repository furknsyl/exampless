##bar chart
import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

df=pd.read_csv('populations.csv')

data=[go.Bar(
    x=df['NOS'],
    y=df['POPULATIONS']
)]

layout=go.Layout(

     title='City populations in Turkey'
)

fig=go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='bar.html')