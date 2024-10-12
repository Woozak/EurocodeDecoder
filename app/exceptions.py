from fastapi import HTTPException, status


class BaseHTTPException(HTTPException):
    status_code = 400
    detail = ''

    def __init__(self):
        super().__init__(status_code=self.status_code, detail=self.detail)


class InvalidEurocodeError(BaseHTTPException):
    status_code = status.HTTP_400_BAD_REQUEST
    detail = 'Invalid Eurocode'


class EurocodeNotFoundError(BaseHTTPException):
    status_code = status.HTTP_404_NOT_FOUND
    detail = 'Eurocode Not Found'
