from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime, timezone

# Post schema
class PostModel(BaseModel):
    image_url: str = Field(..., alias="imageUrl")
   # public_id: str = Field(..., alias="publicId")
   # caption: str
   # hashtags: List[str]
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    class Config:
        populate_by_name = True
        json_schema_extra = {
            "example":{
                "imgaeUrl":"https://res.cloudinary...",
               # "caption":"A beautiful sunset",
               # "hashtags": ["#sunset","#nature"]
            }
        }