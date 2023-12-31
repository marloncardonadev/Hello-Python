from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter(prefix="/users", tags=["users"], responses={404: {"message": "No encontrado"}})

# Entidad user
class User(BaseModel):
    id: int
    name: str
    surname: str
    url: str
    age: int

users = [User(id=1, name="Marlon", surname="Cardona", url="https://moure.dev", age=35),
         User(id=2, name="Zaray", surname="Perez", url="https://moure.dev", age=19),
         User(id=3, name="Patricia", surname="Jaramillo", url="https://moure.dev", age=55)]

@router.get("/")
async def usersJson():
    return users

@router.get("/{id}") # Path
async def usersJson(id: int):
    return search_user(id)

@router.get("/") # Query
async def usersJson(id: int):
    return search_user(id)

@router.post("/", response_model=User, status_code=201)
async def user(user: User):
    if type(search_user(user.id)) == User:
        raise HTTPException(status_code=404, detail="El usuario con el id: " + str(user.id) + " ya existe.")
    users.append(user)
    return user

@router.put("/")
async def user(user: User):
    found = False
    for index, saved_user in enumerate(users):
        if saved_user.id == user.id:
            users[index] = user
            found = True
    if not found:
        return {"Error": "No se actualizo el usuario con el id: " + str(user.id)}
    return user

@router.delete("/{id}")
async def user(id: int):
    found = False
    for index, delete_user in enumerate(users):
        if delete_user.id == id:
            del users[index]
            found = True
    if not found:
        return {"Error": "No se elimino el usuario con el id: " + str(id)}
    return {"Ok": "Se elimino el usuario con el id: " + str(id)}

def search_user(id: int):
    user = filter(lambda user: user.id == id, users)
    try:
        return list(user)[0]
    except:
        return {"Error": "No se encontro un usuario con el id: " + str(id)}

