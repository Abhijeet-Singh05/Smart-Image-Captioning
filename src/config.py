import os
from dotenv import load_dotenv

# to load .env file
load_dotenv()

# to to giving values
class Config():
    # we use .get() to get values from .env file it returns none if empty
    PORT = os.getenv("PORT")
    DB_NAME = "captionDB"
    MONGO_URI = os.getenv("MONGO_URI")
    CLOUDINARY_CLOUD_NAME = os.getenv("CLOUDINARY_CLOUD_NAME")
    CLOUDINARY_API_KEY = os.getenv("CLOUDINARY_API_KEY")
    CLOUDINARY_API_SECRET = os.getenv("CLOUDINARY_API_SECRET")


config = Config()