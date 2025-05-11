from fastapi import FastAPI
from app.models import Item, User
from fastapi import HTTPException

app = FastAPI()

items = [
    Item(id=1, name="Laptop", price=1299.99, in_stock=True),
    Item(id=2, name="Mouse", price=25.50, in_stock=True),
    Item(id=3, name="Mechanical Keyboard", price=89.90, in_stock=False),
    Item(id=4, name='Monitor 24"', price=179.00, in_stock=True),
    Item(id=5, name="USB-C Hub", price=45.00, in_stock=False),
]

users = [
    User(id=1, username="alice", email="alice@example.com"),
    User(id=2, username="bob", email="bob@example.com"),
    User(id=3, username="charlie", email="charlie@example.com"),
]


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
