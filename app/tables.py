from piccolo.table import Table
from piccolo.columns import UUID, Varchar, Date

class User(Table, tablename="users"):
    id = UUID(primary_key=True)
    email = Varchar(unique=True, required=True)
    username = Varchar(required=True)
    birth_date = Date(required=True)
    phone = Varchar(null=True)