from fastapi import APIRouter, UploadFile, File
from src.controllers.post_controller import create_smart_post

router = APIRouter()

@router.post("/upload")
async def upload_image_route(file: UploadFile = File(...)):
    """
    Docstring for upload_image_route
    
    :param file: Description
    :type file: UploadFile

    Route to upload image
    """

    return await create_smart_post(file)