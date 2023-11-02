import streamlit as st
import plotly.graph_objects as go
import calendar
from datetime import datetime

label = ["income", "total income", "other income", "rent", 'food']
source = [0, 1, 2, 2]
target = [2, 2, 3, 4]
value = [10, 2, 6, 4]

link = dict(source=source, target=target, value=value)
node = dict(label=label, pad=50, thickness=5)
data= go.Sankey(link=link, node=node)

fig = go.Figure(data)
fig.show()
