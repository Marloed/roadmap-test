from datetime import datetime

from pydantic import BaseModel, field_validator

class CreateDeviceInput(BaseModel):
    name: str
    ip_address: str
    type: str
    status: str

    @field_validator("name")
    @classmethod
    def validate_name(cls, value):
        if value == "":
            raise ValueError("name is required")
        
        return value
    
    @field_validator("ip_address")
    @classmethod
    def validate_ip_address(cls, value):
        if value == "":
            raise ValueError("ip_address is required")
        
        return value
    
    @field_validator("type")
    @classmethod
    def validate_type(cls, value):
        if value == "":
            raise ValueError("type is required")
        
        return value
    
    @field_validator("status")
    @classmethod
    def validate_status(cls, value):
        if value == "":
            raise ValueError("status is required")
        
        return value
    
class DevicePublicOutput(BaseModel):
    id: str
    name: str
    ip_address: str
    type: str
    status: str
        
class DeviceDetailOutput(BaseModel):
    id: str
    name: str
    ip_address: str
    type: str
    status: str
    updated_at: datetime
    created_at: datetime
    
class UpdateDeviceStatusInput(BaseModel):
    status: str
    
    @field_validator("status")
    @classmethod
    def validate_status(cls, value):
        if value == "":
            raise ValueError("status is required")
        
        return value