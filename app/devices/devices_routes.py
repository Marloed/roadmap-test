from blacksheep import Request, get, post, put
from pydantic import ValidationError

from app.devices.devices_schemas import (
    CreateDeviceInput,
    UpdateDeviceStatusInput)

from app.devices.devices_service import (
    get_all_devices,
    get_device_detail_by_id,
    create_device_in_db,
    find_device_by_id_raw,
    update_device_status_in_db,
)

from app.request_utils import read_json_body
from app.responses import (
    error_response,
    status_response,
    validation_error_response
)

@get("/devices")
async def get_devices():
    devices = await get_all_devices()
    return devices

@get("/devices/{device_id}")
async def get_device_by_id(device_id: str):
    device = await get_device_detail_by_id(device_id)
    
    if device is None:
        return error_response("device not found", 404)
    
    return device

@post("/devices")
async def create_device(request: Request):
    data, error = await read_json_body(request)
    if error is not None: 
        return error_response(error, 400)
    
    try:
        input_data = CreateDeviceInput(**data)
    except ValidationError as error:
        return validation_error_response(error)
    
    await create_device_in_db(
        name=input_data.name,
        ip_address=input_data.ip_address,
        type=input_data.type,
        status=input_data.status,
    )
    
    return status_response("created", 201)

@put("/devices/{device_id}/status")
async def update_device_status(device_id: str, request: Request):
    data, error = await read_json_body(request)
    if error is not None:
        return error_response(error, 400)
    
    try:
        input_data = UpdateDeviceStatusInput(**data)
    except ValidationError as error:
        return validation_error_response(error)
    
    device = await find_device_by_id_raw(device_id)
    
    if device is None:
        return error_response("device not found", 404)
    
    await update_device_status_in_db(
        device_id=device_id,
        status=input_data.status,
    )
    
    return status_response("updated")