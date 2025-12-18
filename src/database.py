from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from src.config import config
from src.utils.api_error import apiError
import sys

#Global variable to hold DB connection
db_client = None
db = None

def connect_to_mongo():
    """
    Docstring for connect_to_mongo
    it connect mongoDB using URI from config
    """

    global db_client,db

    try: 
        # create the client
        db_client = MongoClient(config.MONGO_URI)
        
        db = db_client[config.DB_NAME]

        print(f"Successfully connected to database")

    except ConnectionFailure as e:
        print(f"Could not connect to database. {e}")
    except Exception as e:
        print(f"Unexcepted Database ERROR: {e}")

def close_mongo_connection():
    """
    Docstring for close_mongo_connection
    to close the connection when the app stops.
    """

    global db_client

    if db_client:
        db_client.close()
        print("MongoDB connection closed")


def get_db():

    global db
    
    if db is None:
        raise apiError(500,"Database connection is not initialized.")
    
    return db