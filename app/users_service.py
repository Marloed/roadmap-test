from app.tables import User
from app.users_schemas import UserPublicOutput, UserDetailOutput


def serialize_user_public(user):
    return UserPublicOutput(
        email=user["email"],
        username=user["username"],
    ).model_dump()


def serialize_user_detail(user):
    return UserDetailOutput(
        id=str(user["id"]),
        email=user["email"],
        username=user["username"],
        birth_date=user["birth_date"],
        phone=user["phone"],
    ).model_dump()


async def find_user_by_email(email):
    users = await User.select().where(
        User.email == email
    ).run()

    if len(users) == 0:
        return None

    return serialize_user_detail(users[0])


async def create_user_in_db(email, username, birth_date, phone: str):
    user = User(
        email=email,
        username=username,
        birth_date=birth_date,
        phone=phone,
    )

    await user.save().run()


async def update_user_phone_in_db(email, phone):
    await User.update({
        User.phone: phone,
    }).where(
        User.email == email
    ).run()


async def delete_user_by_email_in_db(email):
    await User.delete().where(
        User.email == email
    ).run()


async def get_all_users() -> dict:
    users = await User.select(
        User.email,
        User.username,
    ).run()

    return [
        serialize_user_public(user)
        for user in users
    ]


async def get_users_without_phone_from_db():
    users = await User.select(
        User.email,
        User.username,
    ).where(
        User.phone == ""
    ).run()

    return [
        serialize_user_public(user)
        for user in users
    ]


async def get_users_with_phone_from_db():
    users = await User.select(
        User.email,
        User.username,
    ).where(
        User.phone != ""
    ).run()

    return [
        serialize_user_public(user)
        for user in users
    ]


async def get_adult_users_from_db(border_date):
    users = await User.select(
        User.email,
        User.username,
    ).where(
        User.birth_date <= border_date
    ).run()

    return [
        serialize_user_public(user)
        for user in users
    ]


async def get_minor_users_from_db(border_date):
    users = await User.select(
        User.email,
        User.username,
    ).where(
        User.birth_date > border_date
    ).run()

    return [
        serialize_user_public(user)
        for user in users
    ]