from fastapi import FastAPI
from routers import products, users, basic_auth_users,jwt_auth_users
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.include_router(products.router)
app.include_router(users.router)
app.include_router(basic_auth_users.router)
app.include_router(jwt_auth_users.router)
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/url")
async def root():
    return {"url_curso": "https://mouredev.com/python"}