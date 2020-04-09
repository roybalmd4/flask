import pandas
import plotly
import plotly.graph_objs as go
import json

def create_plot_scatter(df):

    data = [
        go.Scatter(
            x=df['DOY'], # assign x as the dataframe column 'DOY'
            y=df['Air Max']
        )
    ]

    graphJSON = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)

    return graphJSON

def create_plot_bar(df):
    
    data = [
        go.Bar(
            x=df['DOY'], # assign x as the dataframe column 'DOY'
            y=df['Air Max']
        )
    ]

    graphJSON = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)

    return graphJSON