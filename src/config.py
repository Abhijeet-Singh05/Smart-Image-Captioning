import os
from dotenv import load_dotenv

# to load .env file
load_dotenv()

# to to giving values
class Config():
    # we use .get() to get values from .env file it returns none if empty
    PORT = os.getenv("PORT")
    MONGO_URI = os.getenv("MONGO_URI")


config = Config()