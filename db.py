from sqlalchemy import create_engine
import psycopg2

def localDB():

    engine = create_engine('postgresql://postgres:*********@localhost:5432/test')

    return engine

def awsDB():

    engine = create_engine('postgresql://postgres:*********@htp.ctbdjodkkbuz.us-west-1.rds.amazonaws.com:5432/htp')

    return engine



    
