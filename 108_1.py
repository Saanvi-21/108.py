import pandas as pd 
import csv
import plotly.figure_factory as ff
df = pd.read_csv('108.csv')
fig = ff.create_distplot([df['Height(Inches)'].tolist()], ['Height'], show_hist=True)
fig2 = ff.create_distplot([df['Weight(Pounds)'].tolist()], ['Weight'], show_hist=True)
fig2.show()
