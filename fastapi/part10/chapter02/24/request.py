from fastapi import FastAPI, Request

app = FastAPI()


@app.get("/items/{item_id}")
def read_root(item_id: str, request: Request):
    print("%s: %s" % (str(type(request.state)), request.state.__dict__))
    client_host = request.client.host
    return {"request": client_host, "item_id": item_id}
