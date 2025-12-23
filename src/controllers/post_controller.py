from fastapi import UploadFile
from src.database import get_db
from src.services.cloud_service import upload_to_cloud
from src.models.post_model import PostModel
from src.utils.api_response import apiResponse
from src.utils.api_error import apiError

async def create_smart_post(file: UploadFile):
    """
    Docstring for create_smart_post
    -> upload image to cloudinary
    -> save everything to mongoDB
    """

    # Validation: check it its an image
    if not file.content_type.startswith("image/"):
        raise apiError(
            400,
            "File must be an image"
        )
    
    # Read file: read bytes once so we can use them later
    file_content = await file.read()

    # UPLOAD on cloudinary
    cloud_data = upload_to_cloud(file_content)

    # MODEL
    new_post = PostModel(
        imageUrl=cloud_data["secure_url"],
        publicId=cloud_data["public_id"],
    )

    # Save to mongoDB
    db = get_db()

    result = db["posts"].insert_one(
        new_post.model_dump(by_alias=True)
    )

    # Return response
    return apiResponse(
        message="Post created successfully",
        data ={
            "id": str(result.inserted_id)
        }
    ).dict()


