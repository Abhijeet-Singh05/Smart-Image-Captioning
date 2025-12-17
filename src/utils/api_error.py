from fastapi import HTTPException
class apiError(HTTPException):
    def __init__(self,status_code:int,message:str,errors:list = None):
        super().__init__(status_code=status_code,detail=message)
        self.errors = errors