import streamlit as st
import pandas as pd
import plotly.io as pio


st.write("Here's our first attempt at using data to create a table:")
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))

import plotly.graph_objs as go
from plotly.subplots import make_subplots


df_1 = pd.read_csv('NCS_18_22.csv', encoding='euc-kr', index_col=0)
# df_1 = pd.read_csv('/content/NCS_18_22 (1).csv', encoding='ISO-8859-1')


for col in df_1:
  # print(v)
  df_1[col] = df_1[col].str.replace(',', '').astype(int)


# read in the CSV file
df_1
# create the bar chart
fig = go.Figure(
    go.Bar(
        x=df_1.index,  # x-axis values
        y=df_1["수료훈련생수"],  # y-axis values
        marker_color="#17B897"  # color of the bars
    )
)

# set the title and axis labels
fig.update_layout(
    title="연간 NCS 코드 ",
    xaxis_title="연도",
    yaxis_title="명",
    legend_title="Year",
    xaxis=dict(tickmode='linear', tick0=2019, dtick=1),  # set tick values for x-axis
    yaxis=dict(range=[0, max(df_1["수료훈련생수"]) + 100])  # set range of y-axis
)

# set the range of y-axis
fig.update_layout(
    yaxis=dict(range=[0, max(df_1["수료훈련생수"]) + 100])  # add buffer of 100 to the max value
)


# show the chart
fig.show()
