# -*- coding: utf-8 -*-
"""
Created on Thu Jul 13 17:14:15 2023

@author: s371550
"""

import numpy as np
import plotly.graph_objects as go
import plotly.offline as pyo

np.random.seed(56)

x_val = np.linspace(0,1,100)
y_val = np.random.randn(100)

# create line chart
# each line chart in plotly is called a trace which is then put on the figure

trace0 = go.Scatter(x = x_val,
                   y = y_val+5,
                   mode = 'markers',
                   name = 'markers'
                   )

trace1 = go.Scatter(x = x_val,
                   y = y_val,
                   mode = 'lines',
                   name = 'lines'
                   )

# data = [trace]
# the benefit of data being a list is that you can add many plots as traces in 
# the list

data = [trace0,trace1]

layout = go.Layout(title='line charts')


fig = go.Figure(data,layout)

pyo.plot(fig, 'scatter')