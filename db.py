from sqlalchemy import create_engine
import psycopg2

def localDB():

    engine = create_engine('postgresql://postgres:1q@W3e$R5t^Y@localhost:5432/test')

    return engine

def awsDB():

    engine = create_engine('postgresql://postgres:5t^Y7u*I9o)P@htp.ctbdjodkkbuz.us-west-1.rds.amazonaws.com:5432/htp')

    return engine



    