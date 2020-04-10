from flask import Flask, request, render_template, session, redirect
import pandas as pd
import datetime
import db     # Database connection local or remote
import graphs # Plotly graph function

app = Flask(__name__)

# Read the AZMET daily data directly from the AZMET website.  
df1 = pd.read_csv("https://cals.arizona.edu/AZMET/data/0620rd.txt", header=None)

# Set the column headers since the text file only contains the data.
df1.columns = ['Year', 
            'DOY',
            'Station Num',
            'Air Max',
            'Air Min',
            'Air Mean',
            'RH Max',
            'RS Min',
            'RH Mean',
            'VPD Mean',
            'Solar Rad',
            'Precip',
            'Four Soil Temp Max',
            'Four Soil Temp Min',
            'Four Soil Temp Mean',
            'Twenty Soil Temp Max',
            'Twenty Soil Temp Min',
            'Twenty Soil Temp Mean',
            'Wind Speed',
            'Wind Vec Mag',
            'Wind Vec Dir',
            'Wind Dir StDev',
            'Max Wind Speed',
            'Heat Units',
            'Ref Evapo',
            'Ref Evapo Pen',
            'Actual Vap',
            'Dewpoint Daily']

# Creating df2 and filtering down to two columns from df1.  These two columns will
# be displayed.
df2 = df1.filter(items=['DOY','Air Max'])

# Comment 4/8 for testing branchs
# This is for testing purposes. Comment out when ready for production.
theTime = datetime.datetime.now()
print(f'Starting database insert {theTime}')

#  Insert the data from AZMET into the database. Calling postDB to get the connection 
#  object to the database.
# df1.to_sql('azmet', db.localDB(), if_exists='append')

# ** This function connects to an AWS instance and does an insert.
# df1.to_sql('azmet', db.awsDB(), if_exists='append')

# Show the time that the db insert completed
print(f'Done with database insert {theTime}')

# Home directory for the application. Uses home.html.
@app.route('/', methods=("POST", "GET"))
def home():

    return render_template('home.html', name="AZMET Data", data=df2.to_html())

# /graph to get to this page.  Uses graph.html.
# @app.route('/graph', methods=("POST", "GET"))
# def graph():

#     bar = graphs.create_plot(df2)
#     return render_template('graph.html', name="AZMET Graph", plot=bar)

# /graph to get to this page.  Uses graph.html.
@app.route('/scatter', methods=("POST", "GET"))
def scatter():

    # Function requires a dataframe and type of graph
    scatter = graphs.create_plot(df2, "Scatter")
    return render_template('scatter.html', name="AZMET Graph", plot=scatter)

@app.route('/bar', methods=("POST", "GET"))
def bar():

    # Function requires a dataframe and type of graph
    bar = graphs.create_plot(df2, "Bar")
    return render_template('bar.html', name="AZMET Graph", plot=bar)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)