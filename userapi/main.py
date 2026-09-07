from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel


app = FastAPI()


all_users = []

next_user_id = 1


class UserCreate(BaseModel):
    name: str
    email: str


class UserResponse(BaseModel):
    id: int
    name: str
    email: str


@app.get("/users")
def get_users():
    return all_users


@app.get(
    "/users/{user_id}",
    response_model=UserResponse
)
def get_user(user_id: int):

    for user in all_users:

        if user["id"] == user_id:
            return user

    raise HTTPException(
        status_code=404,
        detail="User not found"
    )


@app.post(
    "/users",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED
)
def create_user(user: UserCreate):

    global next_user_id

    new_user = {
        "id": next_user_id,
        "name": user.name,
        "email": user.email
    }

    all_users.append(new_user)

    next_user_id = next_user_id + 1

    return new_user


@app.put(
    "/users/{user_id}",
    response_model=UserResponse
)
def update_user(user_id: int, user: UserCreate):

    for index in range(len(all_users)):

        current_user = all_users[index]

        if current_user["id"] == user_id:

            updated_user = {
                "id": user_id,
                "name": user.name,
                "email": user.email
            }

            all_users[index] = updated_user

            return updated_user

    raise HTTPException(
        status_code=404,
        detail="User not found"
    )


@app.delete("/users/{user_id}")
def delete_user(user_id: int):

    for index in range(len(all_users)):

        current_user = all_users[index]

        if current_user["id"] == user_id:

            deleted_user = all_users.pop(index)

            return {
                "message": "User deleted successfully",
                "user": deleted_user
            }

    raise HTTPException(
        status_code=404,
        detail="User not found"
    )