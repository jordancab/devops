from fastapi import FastAPI
from app.models import Item, User
from requests import HTTPException
app = FastAPI()

items = []
users = []


@app.get("/items")
def get_items():
    return items


@app.get("/items/{item_id}")
def get_item(item_id: int):
    for item in items:
        if item.id == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")


@app.post("/items")
def create_item(item: Item):
    items.append(item)
    return item


@app.put("/items/{item_id}")
def update_item(item_id: int, updated_item: Item):
    for index, item in enumerate(items):
        if item.id == item_id:
            items[index] = updated_item
            return updated_item
    raise HTTPException(status_code=404, detail="Item not found")


@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    for index, item in enumerate(items):
        if item.id == item_id:
            del items[index]
            return {"message": "Item deleted"}
    raise HTTPException(status_code=404, detail="Item not found")


# --- Bonus : User Endpoints ---


@app.get("/users")
def get_users():
    return users


@app.post("/users")
def create_user(user: User):
    users.append(user)
    return user
