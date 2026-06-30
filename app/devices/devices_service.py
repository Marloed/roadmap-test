from app.tables import Device
from app.devices.devices_schemas import DevicePublicOutput, DeviceDetailOutput
from datetime import datetime


def serialize_device_public(device):
    return DevicePublicOutput(
        id=str(device["id"]),
        name=device["name"],
        ip_address=device["ip_address"],
        type=device["type"],
        status=device["status"],
    ).model_dump()
    
def serialize_device_detail(device):
    return DeviceDetailOutput(
        id=str(device["id"]),
        name=device["name"],
        ip_address=device["ip_address"],
        type=device["type"],
        status=device["status"],
        created_at=device["created_at"],
        updated_at=device["updated_at"],
    ).model_dump()
    
async def get_all_devices():
    devices = await Device.select(
        Device.id,
        Device.name,
        Device.ip_address,
        Device.type,
        Device.status,
    )
    
    return [
        serialize_device_public(device)
        for device in devices
    ]
    
async def find_device_by_id_raw(device_id):
    devices = await Device.select().where(
        Device.id == device_id
    )
    
    if len(devices) == 0:
        return None
    
    return devices[0]

async def create_device_in_db(name, ip_address, type, status):
    device = Device(
        name=name,
        ip_address=ip_address,
        type=type,
        status=status,
    )
    
    await device.save()
    
async def update_device_status_in_db(device_id, status):
    await Device.update({
        Device.status: status,
        Device.updated_at: datetime.now(),
    }).where(
        Device.id == device_id
    )
    
async def update_device_in_db(device_id, name, ip_address, type, status):
    device = await find_device_by_id_raw(device_id)
    
    if device is None:
        return None
    
    await Device.update({
        Device.name: name,
        Device.ip_address: ip_address,
        Device.type: type,
        Device.status: status,
    })