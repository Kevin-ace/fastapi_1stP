from typing import List
from uuid import UUID 
from fastapi import FastAPI, HTTPException
from models import User,Gender,Role


app=FastAPI()

db: List[User] = [User(id=UUID("f55c281e-832b-4e89-b189-2ba4f82e1ecb"),
                       first_name="John",
                        last_name="Doe",
                        gender=Gender.male, 
                        roles=[Role.intern]),
                  User(id=UUID("c2722ec9-79a2-450b-9955-0ff815ef00bb"),
                       first_name="Laura",
                        last_name="Mary",
                        gender=Gender.female, 
                        roles=[Role.admin, Role.user])
                  ]

@app.get('/')
def root():
    return{"Hello": "Kev"}

@app.get("/api/v1/users")
async def fetch_users():
    return db;

@app.post("/api/v1/users")
async def register_users(user: User):
    db.append(user)
    return {id: user.id}

@app.delete("/api/v1/users/{user_id}")
async def delete_user(user_id: UUID):
    for user in db:
        if user.id == user_id:
            db.remove(user)
            return
    raise HTTPException(status_code=404, detail=f"User with id:{user_id} not found")