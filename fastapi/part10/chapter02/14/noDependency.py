from fastapi import FastAPI

app = FastAPI()

@app.get("/items/")
async def read_items(q: str | None = None, skip: int = 0, limit: int = 100):
    return {'q': q, 'skip': skip, 'limit': limit}


@app.get("/users/")
async def read_users(q: str | None = None, skip: int = 0, limit: int = 100):
    return {'q': q, 'skip': skip, 'limit': limit}
