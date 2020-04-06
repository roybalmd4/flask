from flask import Flask, request, render_template, session, redirect
import pandas as pd
import datetime
import db

app = Flask(__name__)

df1 = pd.read_csv("https://cals.arizona.edu/AZMET/data/0620rd.txt", header=False)
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

df2 = df1.filter(items=['DOY','Air Max'])

theTime = datetime.datetime.now()
print(f'Starting database insert {theTime}')
#  ** This function connects to the local database and does an insert
# df1.to_sql('azmet', conn = db.postDB(), if_exists='append')

# ** This function connects to an AWS instance and does an insert.
df1.to_sql('azmet', conn = db.awsDB(), if_exists='append')
print(f'Done with database insert {theTime}')
conn.close()

@app.route('/', methods=("POST", "GET"))
def home():

    return render_template('home.html', name="AZMET Data", data=df2.to_html())

@app.route('/graph', methods=("POST", "GET"))
def graph():

    return render_template('graph.html', name="AZMET Graph", data=df2.to_html())


if __name__ == '__main__':
    app.run(host='0.0.0.0')