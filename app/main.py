import uvicorn
from fastapi import FastAPI, status

from app.utils import get_glass_info
from app.glass_schemas import ResponseGlass


app = FastAPI()


@app.get(
    '/decode/{eurocode}',
    response_model=ResponseGlass,
    response_model_exclude_defaults=True,
    status_code=status.HTTP_200_OK
)
def decode(eurocode: str):
    return get_glass_info(eurocode)


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
