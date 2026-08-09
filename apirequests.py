from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


# ---------------- USER MODEL ----------------

class User(BaseModel):
    name: str
    age: int
    email: str


# ---------------- DATABASE ----------------

users = {
    1: {
        "name": "Naveen Kumar111",
        "age": 19,
        "email": "naveen@gmail.com"
    },
    2: {
        "name": "Sanjay Kumar",
        "age": 20,
        "email": "sanjay@gmail.com"
    }
}


# ==================================================
# 1. GET
# ==================================================

@app.get("/users/{user_id}")
def user_profile(user_id: int):

    if user_id not in users:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )
    return {
        "user_id": user_id,
        "user": users[user_id]
    }

@app.get("/users")
def display_all_users():
    return {
        "users": users
    }
# ==================================================
# 2. POST
# ==================================================

@app.post("/users")
def create_user(user: User):

    new_id = max(users.keys()) + 1

    users[new_id] = {
        "name": user.name,
        "age": user.age,
        "email": user.email
    }
    return {
        "message": "User created successfully",
        "user_id": new_id,
        "user": users[new_id]
    }


# ==================================================
# 3. PUT
# ==================================================

@app.put("/users/{user_id}")
def update_user(user_id: int, user: User):

    if user_id not in users:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    users[user_id] = {
        "name": user.name,
        "age": user.age,
        "email": user.email
    }

    return {
        "message": "User completely updated",
        "user": users[user_id]
    }


# ==================================================
# 4. PATCH
# ==================================================

@app.patch("/users/{user_id}")
def partial_update_user(user_id: int, user: dict):

    if user_id not in users:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    users[user_id].update(user)

    return {
        "message": "User partially updated",
        "user": users[user_id]
    }


# ==================================================
# 5. DELETE
# ==================================================

@app.delete("/users/{user_id}")
def delete_user(user_id: int):

    if user_id not in users:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    deleted_user = users.pop(user_id)

    return {
        "message": "User deleted successfully",
        "user": deleted_user
    }