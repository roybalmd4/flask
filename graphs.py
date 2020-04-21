import pandas
import plotly
import plotly.graph_objs as go
import json

#  There are comments made on 4/21/2020

# Passing the dataframe and also the graph type.
def create_plot(df, graph_type):

    # Thinned two functions down to one.

    if graph_type == "Scatter":
        data = [
            go.Scatter(x=df['DOY'], # assign x as the dataframe column 'DOY'
                       y=df['Air Max'])
        ]
    else:
        data = [
            go.Bar(x=df['DOY'], # assign x as the dataframe column 'DOY'
                   y=df['Air Max'])
        ]

    graphJSON = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)

    return graphJSON

