from flask import Flask, request, render_template, session, redirect
import pandas as pd


app = Flask(__name__)

df1 = pd.read_csv("https://cals.arizona.edu/AZMET/data/0620rd.txt")
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

@app.route('/', methods=("POST", "GET"))
def html_table():

    return render_template('simple.html',  tables=[df1.to_html(classes='data')], titles=df.columns.values)



if __name__ == '__main__':
    app.run(host='0.0.0.0')