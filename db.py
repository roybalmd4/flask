from sqlalchemy import create_engine
import psycopg2

# Connecting to the local Postgresql database for testing purposes.  Change to 
# awsDB() when moving to production.
def localDB():

    engine = create_engine('postgresql://postgres:*******@localhost:5432/test')

    return engine

# Use awsDB for production.  More information about the database can be seen in the 
# AWS Console -> RDS -> HTP
def awsDB():

    # Connect to the database and return a connection object into engine
    engine = create_engine('postgresql://postgres:*********@htp.ctbdjodkkbuz.us-west-1.rds.amazonaws.com:5432/htp')

    # Return the connection object to the caller.
    return engine



    
