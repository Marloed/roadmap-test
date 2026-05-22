from app.tables import User

async def find_user_by_email(email):
    users = await User.select().where(
        User.email == email
    ).run()
    
    if len(users) == 0:
        return None
    
    return users[0]

async def create_user_in_db(email, username, birth_date, phone):
    user = User(
        email=email,
        username=username,
        birth_date=birth_date,
        phone=phone
    )
    
    await user.save().run()
    
async def update_user_phone_in_db(email, phone):
    await User.update({
        User.phone: phone
    }).where(
        User.email == email
    ).run()
    
async def delete_user_by_email_in_db(email):
    await User.delete().where(
        User.email == email
    ).run()
    
async def get_all_users():
    return await User.select(
        User.email,
        User.username,
    ).run()
    
async def get_users_without_phone_from_db():
    return await User.select(
        User.email,
        User.username,
    ).where(
        User.phone == ""
    ).run()
    
async def get_users_with_phone_from_db():
    return await User.select(
        User.email,
        User.username,
    ).where(
        User.phone != ""
    ).run()
    
async def get_adult_users_from_db(border_date):
    return await User.select(
        User.email,
        User.username,
    ).where(
        User.birth_date <= border_date
    ).run()
    
async def get_minor_users_from_db(border_date):
    return await User.select(
        User.email,
        User.username,
    ).where(
        User.birth_date > border_date
    ).run()