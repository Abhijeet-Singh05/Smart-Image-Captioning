
class apiResponse:
    def __init__(self,message: str, data: any = None, status_code: int = 200):
        self.message= message
        self.data= data
        self.success= status_code < 400

    def dict(self):
        return {
            "success": self.success,
            "message": self.message,
            "data": self.data
        }
    