from blacksheep import get, post, put, FromJSON

from app.devices.devices_schemas import (
    CreateDeviceInput,
    UpdateDeviceStatusInput)

from app.devices.devices_service import (
    get_all_devices,
    serialize_device_detail,
    create_device_in_db,
    find_device_by_id_raw,
    update_device_status_in_db,
)

from app.responses import (
    error_response,
    status_response,
)

@get("/devices")
async def get_devices():
    devices = await get_all_devices()
    return devices

@get("/devices/{device_id}")
async def get_device_by_id(device_id: str):
    device = await find_device_by_id_raw(device_id)
    
    if device is None:
        return error_response("device not found", 404)
    
    return serialize_device_detail(device)

@post("/devices")
async def create_device(body: FromJSON[CreateDeviceInput]):
    input_data = body.value
    
    await create_device_in_db(
        name=input_data.name,
        ip_address=input_data.ip_address,
        type=input_data.type,
        status=input_data.status,
    )
    
    return status_response("created", 201)
    

@put("/devices/{device_id}/status")
async def update_device_status(device_id: str, body: FromJSON[UpdateDeviceStatusInput]):
    update_data = body.value
    
    device = await find_device_by_id_raw(device_id)
    
    if device is None:
        return error_response("device not found", 404)
    
    await update_device_status_in_db(
        device_id=device_id,
        status=update_data.status,
    )
    
    return status_response("updated")