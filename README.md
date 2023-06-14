# Project

## Charts

- Bar Chart
- Pie Chart
- Tems Chart
- Tourism Chart

## Onlinegdb

- Largest Palindrome
- Largest Prime
- Letters
- Letters2
- MultipleBelow
- Smallest Multiple

## Website

- Templates
- Flask.app


```Code
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


```