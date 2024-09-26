from fastapi import FastAPI, status


app = FastAPI()


@app.get('/decode/{eurocode}', status_code=status.HTTP_200_OK)
def decode_eurocode():
    pass
