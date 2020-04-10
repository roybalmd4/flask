import pandas as pd
import psycopg2
from sqlalchemy import create_engine
import datetime

# Made comments

def make_connection():
    '''
        Establish the connection to the database and provide
        the caller with a connection object.

        INPUTS : None
        OUTPUTS: Connection object (RETURN conn)
        AWS Instance: 5t^Y7u*I9o)P

    '''

    engine = create_engine('postgresql://postgres:1q@W3e$R5t^Y@htp.ctbdjodkkbuz.us-west-1.rds.amazonaws.com:5432/azmet')

    df1 = pd.read_csv("https://cals.arizona.edu/AZMET/data/0620rd.txt")
    df1.columns = [ 'Year', 
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

    