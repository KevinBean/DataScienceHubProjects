This is a project from https://thecleverprogrammer.com/2022/05/31/smartwatch-data-analysis-using-python/.

From this project, the following purposes are achieved:

# The basic use of pandas
import pandas as pd

## Use pandas to import a csv file
pd.read_scv()

## Preview the data
- data.head()
- data.isnull().sum()
- data.info()
- data.describe()
- data.sample(5)

## Data operation
- data["column_new"] = data["column_1"] + data["column_2"]
- data["column"].value_counts()

## Format datetime with pandas
- pd.to_datatime(data["column"], format="%m/%d/%Y")
- data["Date"].dt.day_name()

# Plotly to visulase data
- import plotly.express as px
- import plotly.graph_objects as go

## graph
- scatter
- bar
- chart
