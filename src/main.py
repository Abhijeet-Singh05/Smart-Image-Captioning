from fastapi import FastAPI
from contextlib import asynccontextmanager
from fastapi.staticfiles import StaticFiles

# Import Route
from src.routes import post_routes

# Import Database logic
from src.database import connect_to_mongo, close_mongo_connection

# Import Error Handlers
from src.utils.api_error import apiError
from src.utils.exception_handlers import api_error_handler, generic_exception_handler

@asynccontextmanager
async def lifespan(app: FastAPI):
    # connect to DB
    connect_to_mongo()
    yield
    # close DB
    close_mongo_connection()

# App initalization
app = FastAPI(
    title="Smart Image Captioning API",
    version="1.0.0",
    lifespan=lifespan
)

# Error Handling
app.add_exception_handler(apiError,api_error_handler)
app.add_exception_handler(Exception,generic_exception_handler)


# routes
app.include_router(post_routes.router, prefix="/api")

# root route
@app.get("/")
def home():
    return{
        "message":"Smart Caption API is running!",
        "docs":"http://127.0.0.1:8000/docs"
    }