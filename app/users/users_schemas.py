from datetime import date
from pydantic import BaseModel, field_validator

class CreateUserInput(BaseModel):
    email: str
    username: str
    birth_date: date
    phone: str = ""
    
    @field_validator("email")
    @classmethod
    def validate_email(cls, value):
        if value == "":
            raise ValueError("email is required")
        
        return value
    
    @field_validator("username")
    @classmethod
    def validate_username(cls, value):
        if value == "":
            raise ValueError("username is required")
        
        return value
       
class UserPublicOutput(BaseModel):
    email: str
    username: str
    
class UserDetailOutput(BaseModel):
    id: str
    email: str
    username: str
    birth_date: date
    phone: str
     
class UpdateUserPhoneInput(BaseModel):
    phone: str
    
    @field_validator("phone")
    @classmethod
    def validate_phone(cls, value):
        if value == "":
            raise ValueError("phone is required")
        
        return value
