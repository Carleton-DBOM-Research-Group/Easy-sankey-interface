# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 10:58:31 2019

@author: sapta
"""

#%% Libraries
import pandas as pd
import numpy as np
import plotly
import plotly.io as pio

#%%Set up plotly
plotly.tools.set_credentials_file(username='username', api_key='get api key')
plotly.tools.set_config_file(world_readable=True,
                             sharing='public')

#%%Pull out the CSV file with building complaints
raw_dataset = pd.read_csv('~filepath', encoding = "ISO-8859-1")
list = [14,20,17,33,41,28,123,13,26,18,76,126]
indexes = np.array(list)
clean_data = raw_dataset.iloc[:,indexes]

sankey_data = clean_data[clean_data['h_Category'].str.contains("Temperature|Maintenance|Lighting|Janitorial")== True]
list = [3,5]
sankey_indexes = np.array(list)
sankey_data = sankey_data.iloc[:,sankey_indexes]

#%%Set up the sankey diagram
data = dict(
    type='sankey',
    node = dict(
      pad = 15,
      thickness = 20,
      line = dict(
        color = "black",
        width = 0.5
      ),
      label = ["A1", "A2", "B1", "B2", "C1", "C2"],
      color = ["red", "red", "red", "red", "red", "red"]
    ),
    link = dict(
      source = [0,1,0,2,3,3],
      target = [2,3,3,4,4,5],
      value = [8,4,2,8,4,2]
  ))
layout =  dict(
#    title = NULL,
    font = dict(
      size = 20,
      color = 'white'
    ),
    plot_bgcolor = 'white',
    paper_bgcolor = 'white'
)
#%%Plot the sankey
fig = dict(data=[data], layout=layout)
#write image to svg format
pio.write_image(fig, '~filepath\\sankey_py_network.svg')
