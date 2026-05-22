from blacksheep import Request,  get, post, put, delete, json
from datetime import date
from app.responses import error_response, status_response
from app.users_service import (
    find_user_by_email,
    create_user_in_db,
    update_user_phone_in_db,
    delete_user_by_email_in_db,
    get_all_users,
    get_users_with_phone_from_db,
    get_users_without_phone_from_db,
    get_adult_users_from_db,
    get_minor_users_from_db
    )
from asyncpg.exceptions import UniqueViolationError
from app.users_validation import (
    validate_required_user_fields,
    parse_birth_date
    )
@get("/users")
async def get_users():
    users = await get_all_users()
    return users

@get("/users/by-email/{email}")
async def get_user_by_email(email: str):
    user = await find_user_by_email(email)
    
    if user is None:
        return error_response("user not found", 404)
    return user

@get("/users/without-phone")
async def get_users_without_phone():
    users = await get_users_without_phone_from_db()
    return users

@get("/users/with-phone")
async def get_users_with_phone():
    users = await get_users_with_phone_from_db()
    return users


@get("/users/adults")
async def get_users_adults():
    users = await get_adult_users_from_db(date(2008, 5, 18))
    return users

@get("/users/minors")
async def get_users_minors():
    users = await get_minor_users_from_db(date(2008, 5, 18))
    return users

@post("/users")
async def create_user(request: Request):
    data = await request.json()
    error = validate_required_user_fields(data)
    if error is not None:
        return error_response(error["error"], 400)

    birth_date, error = parse_birth_date(data["birth_date"])
    if error is not None:
        return error_response(error["error"], 400)
    
    try:
        await create_user_in_db(
            email=data["email"],
            username=data["username"],
            birth_date=birth_date,
            phone=data.get("phone", "")
        )
    except UniqueViolationError:
        return error_response("email alredy exists", 409)
    
    return status_response("create", 201)

@put("/users/by-email/{email}/phone")
async def update_user_phone(email: str, request: Request):
    data = await request.json()
    
    if "phone" not in data or data["phone"] == "":
        return error_response("phone is required", 400)
    
    user = await find_user_by_email(email)
    
    if user is None:
        return error_response("user not found", 404)
    
    await update_user_phone_in_db(
        email=email,
        phone=data["phone"]
    )
    
    return status_response("updated")

@delete("/users/by-email/{email}")
async def delete_user(email: str):
    user = await find_user_by_email(email)
    
    if user is None:
        return error_response("user not found", 404)
    
    await delete_user_by_email_in_db(email)
    
    return status_response("deleted")