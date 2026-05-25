from blacksheep import Request, get, post, json
import random
from app.tables import User
counter = {
    "total": 0,
    "random": 0,
    "echo": 0
}

def increment_counter(name):
    counter["total"] = counter["total"] + 1
    counter[name] = counter[name] + 1

@get("/random")
def get_random():
    value = random.randint(1, 100)
    increment_counter("random")
    return {"value": value}
    

@post("/echo")
async def post_echo(request: Request):
    data = await request.json()
    increment_counter("echo")
    if "name" not in data or data["name"] == "":
        return {"error": "name is required"}
    elif "age" not in data:
        return {"error": "age is required"}
    elif data["age"] < 0:
        return {"error": "age must be >= 0"}
    data["yourdata"] = "received"
    return data

@get("/counter")
def get_counter():
    return counter

@get("/health")
async def health_check():
    try:
        await User.count().run()
    except Exception:
        return json(
            {"status": "database error"},
            status=503,
        )
    
    return json(
        {"status": "ok"},
        status=200,
    )