from fastapi import Request
from fastapi.responses import JSONResponse
from src.utils.api_error import apiError
from src.utils.api_response import apiResponse

async def api_error_handler(request: Request, exc: apiError):
    """
    Catches our custom Api Errors
    """

    return JSONResponse(
        status_code=exc.status_code,
        content=apiResponse(
            message=exc.detail,
            status_code=exc.status_code,
            data=exc.errors
        ).dict()
    )

async def generic_exception_handler(request: Request, exc: Exception):
    """
    Docstring for generic_exception_handler
    
    Catches everything else
    """

    print(f"Unhandled error: {exc}")

    return JSONResponse(
        status_code=500,
        content=apiResponse(
            message="Internal Server Error!",
            status_code= 500,
            data = {"error": str(exc)}
        ).dict()
    )