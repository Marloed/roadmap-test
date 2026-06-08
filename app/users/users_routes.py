from blacksheep import Request,  get, post, put, delete, json
from datetime import date
from app.responses import (
    error_response, 
    status_response,
    validation_error_response,
    )
from app.users.users_service import (
    find_user_by_email_raw,
    get_user_detail_by_email,
    create_user_in_db,
    update_user_phone_in_db,
    delete_user_by_email_in_db,
    get_all_users,
    get_users_with_phone_from_db,
    get_users_without_phone_from_db,
    get_adult_users_from_db,
    get_minor_users_from_db
    )
from app.users.users_utils import get_adult_border_date
from asyncpg.exceptions import UniqueViolationError
from pydantic import ValidationError
from app.users.users_schemas import (
    CreateUserInput,
    UpdateUserPhoneInput
)
from app.request_utils import read_json_body


@get("/users")
async def get_users():
    users = await get_all_users()
    return users

@get("/users/by-email/{email}")
async def get_user_by_email(email: str):
    user = await get_user_detail_by_email(email)
    
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
    users = await get_adult_users_from_db(get_adult_border_date())
    return users

@get("/users/minors")
async def get_users_minors():
    users = await get_minor_users_from_db(get_adult_border_date())
    return users

@post("/users")
async def create_user(request: Request):
    data, error = await read_json_body(request)
    if error is not None:
        return error_response(error, 400)
    
    try:
        input_data = CreateUserInput(**data)
    except ValidationError as error:
        return validation_error_response(error)
    
    try:
        await create_user_in_db(
            email=input_data.email,
            username=input_data.username,
            birth_date=input_data.birth_date,
            phone=input_data.phone,
        )
    except UniqueViolationError:
        return error_response("email already exists", 409)
    
    return status_response("created", 201)

@put("/users/by-email/{email}/phone")
async def update_user_phone(email: str, request: Request):
    data, error = await read_json_body(request)
    if error is not None:
        return error_response(error, 400)
    
    try:
        input_data = UpdateUserPhoneInput(**data)
    except ValidationError as error:
        return validation_error_response(error)
    
    user = await find_user_by_email_raw(email)
    
    if user is None:
        return error_response("user not found", 404)
    
    await update_user_phone_in_db(
        email=email,
        phone=input_data.phone
    )
    
    return status_response("updated")

@delete("/users/by-email/{email}")
async def delete_user(email: str):
    user = await find_user_by_email_raw(email)
    
    if user is None:
        return error_response("user not found", 404)
    
    await delete_user_by_email_in_db(email)
    
    return status_response("deleted")