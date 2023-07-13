# -*- coding: utf-8 -*-
"""
Created on Mon Jun 19 18:16:45 2023

@author: s371550
"""

import numpy as np
import plotly.offline as pyo
import plotly.graph_objs as go

np.random.seed(42)

# data setup
random_x = np.random.randint(1,101,100)
random_y = np.random.randint(1,101,100)

#basic plots
data = [go.Scatter(x=random_x,y=random_y,
                   mode='markers',
                   marker= dict(
                       size=50,
                       color='#989FCE',
                       symbol='pentagon',
                       line={'width':5}
                       ))]


layout = go.Layout(title='Scatterplot',
                   xaxis={'title':'this is x'},
                   yaxis=dict(title='this is y'),
                   hovermode='closest')

fig = go.Figure(data=data,layout=layout)
pyo.plot(fig, filename='scatter.html')