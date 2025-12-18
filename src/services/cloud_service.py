import cloudinary
import cloudinary.uploader
from src.config import config
from src.utils.api_error import apiError


cloudinary.config(
    cloud_name = config.CLOUDINARY_CLOUD_NAME,
    api_key = config.CLOUDINARY_API_KEY,
    api_secret = config.CLOUDINARY_API_SECRET
)


def upload_to_cloud(file_obj):
    """
    Docstring for upload_to_cloud
    
    :param file_obj: Description

    upload a file to cloudinary

    """

    try: 
        res = cloudinary.uploader.upload(file_obj)
        return res
    
    except Exception as e:
        raise apiError(500, "image upload failed", errors=[str(e)])