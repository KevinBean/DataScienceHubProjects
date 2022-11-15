import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go

data = pd.read_csv("Smartwatch Data Analysis/dailyActivity_merged.csv")
print(data.head()) # preview the data structure
print(data.isnull().sum()) # if there is any null value
print(data.info())

# reform the date column
data["ActivityDate"] = pd.to_datetime(data["ActivityDate"], format="%m/%d/%Y")
print(data.info())

# new column TotalMinutes
data["TotalMinutes"] = data["VeryActiveMinutes"] + data["FairlyActiveMinutes"] + data["LightlyActiveMinutes"] + data["SedentaryMinutes"]
print(data["TotalMinutes"].sample(5))

print(data.describe())

# view the "Calories" column related to steps everyday
figure = px.scatter(data_frame = data, x = "Calories", y="TotalSteps", size="VeryActiveMinutes", 
                    trendline="ols", 
                    title="Relationship between Calories & Total Steps")
figure.show()

# average total number of active munites in a day
label = ["Very Active Minutes", "Fairly Active Minutes", 
         "Lightly Active Minutes", "Inactive Minutes"]
counts = data[["VeryActiveMinutes", "FairlyActiveMinutes", 
               "LightlyActiveMinutes", "SedentaryMinutes"]].mean()
colors = ['gold','lightgreen', "pink", "blue"]
fig = go.Figure(data=[go.Pie(labels=label, values=counts)])
fig.update_layout(title_text='Total Active Minutes')
fig.update_traces(hoverinfo='label+percent', textinfo='value', textfont_size=30,
                  marker=dict(colors=colors, line=dict(color='black', width=3)))
fig.show()

# new column "Day" from the "Date"
data["Day"] = data["ActivityDate"].dt.day_name()
print(data["Day"].head())

# every day's active minutes
fig = go.Figure()
# New traces can be added to a graph object figure using the add_trace() method. This method accepts a graph object trace (an instance of go.Scatter, go.Bar, etc.) and adds it to the figure. This allows you to start with an empty figure, and add traces to it sequentially.
fig.add_trace(go.Bar( x=data["Day"],  y=data["VeryActiveMinutes"], name='Very Active',  marker_color='purple'))
# fig.add_trace(go.Bar(
#     x=data["Day"],
#     y=data["FairlyActiveMinutes"],
#     name='Fairly Active',
#     marker_color='green'
# ))
# fig.add_trace(go.Bar( x=data["Day"], y=data["LightlyActiveMinutes"], name='Lightly Active', marker_color='pink'))
fig.add_bar(x=data["Day"], y=data["LightlyActiveMinutes"], name='Lightly Active', marker_color='pink')
fig.add_bar(x=data["Day"], y=data["FairlyActiveMinutes"], name='Fairly Active', marker_color='green')

fig.update_layout(barmode='group', xaxis_tickangle=-45)
fig.show()

# show inactive minutes in each day
day = data["Day"].value_counts()
label = day.index
counts = data["SedentaryMinutes"]
colors = ['gold','lightgreen', "pink", "blue", "skyblue", "cyan", "orange"]

fig = go.Figure(data=[go.Pie(labels=label, values=counts)])
fig.update_layout(title_text='Inactive Minutes Daily')
fig.update_traces(hoverinfo='label+percent', textinfo='value', textfont_size=30,
                  marker=dict(colors=colors, line=dict(color='black', width=3)))
fig.show()

# show calories in each day
calories = data["Day"].value_counts()
label = calories.index
counts = data["Calories"]
colors = ['gold','lightgreen', "pink", "blue", "skyblue", "cyan", "orange"]

fig = go.Figure(data=[go.Pie(labels=label, values=counts)])
fig.update_layout(title_text='Calories Burned Daily')
fig.update_traces(hoverinfo='label+percent', textinfo='value', textfont_size=30,
                  marker=dict(colors=colors, line=dict(color='black', width=3)))
fig.show()