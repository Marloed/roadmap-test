from piccolo.table import Table
from piccolo.columns import UUID, Varchar, Date, Timestamp

from datetime import datetime

class User(Table, tablename="users"):
    id = UUID(primary_key=True)
    email = Varchar(unique=True, required=True)
    username = Varchar(required=True)
    birth_date = Date(required=True)
    phone = Varchar(null=True)
    
class Device(Table, tablename="devices"):
    id = UUID(primary_key=True)
    name = Varchar(required=True)
    ip_address = Varchar(required=True)
    type = Varchar(required=True)
    status = Varchar(required=True)
    created_at = Timestamp(default=datetime.now)
    updated_at = Timestamp(default=datetime.now)