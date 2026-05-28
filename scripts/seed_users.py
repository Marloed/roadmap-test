import asyncio
from datetime import date

from asyncpg.exceptions import UniqueViolationError

from app.tables import User

TEST_USER = [
    {
        "email": "mark@example.com",
        "username": "Mark",
        "birth_date": date(2000, 5, 10),
        "phone": "+79990000000",
    },
    {
        "email": "alex@example.com",
        "username": "Alex",
        "birth_date": date(2005, 3, 15),
        "phone": "",
    },
    {
        "email": "kid@example.com",
        "username": "Mark",
        "birth_date": date(2012, 1, 1),
        "phone": "",
    }
]

async def create_user(user_data):
    user = User(
        email=user_data["email"],
        username=user_data["username"],
        birth_date=user_data["birth_date"],
        phone=user_data["phone"],
    )
    
    try:
        await user.save().run()
        print(f"created: {user_data['email']}")
    except UniqueViolationError:
        print(f"skipped, already exists: {user_data['email']}")
        
async def main():
    for user_data in TEST_USER:
        await create_user(user_data)
        
if __name__ == "__main__":
    asyncio.run(main())