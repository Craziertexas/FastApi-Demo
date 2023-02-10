from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.openapi.utils import get_openapi

app = FastAPI()

@app.get("/")
async def read_main():
    return {"msg": "Hello World"}

@app.get("/docs")
async def read_openApi():
    return get_openapi(title="FastApi-Demo", version="1.0.0", routes=app.routes)
    
@app.exception_handler(Exception)
async def exception_handler(request, exc):
    return JSONResponse(status_code=500, content={"message": f"Something went wrong :("})