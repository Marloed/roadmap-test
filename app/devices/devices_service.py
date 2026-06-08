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
    ).run()
    
    return [
        serialize_device_public(device)
        for device in devices
    ]
    
async def find_device_by_id_raw(device_id):
    devices = await Device.select().where(
        Device.id == device_id
    ).run()
    
    if len(devices) == 0:
        return None
    
    return devices[0]

async def get_device_detail_by_id(device_id):
    device = await find_device_by_id_raw(device_id)
    
    if device is None:
        return None
    
    return serialize_device_detail(device)

async def create_device_in_db(name, ip_address, type, status):
    device = Device(
        name=name,
        ip_address=ip_address,
        type=type,
        status=status,
    )
    
    await device.save().run()
    
async def update_device_status_in_db(device_id, status):
    await Device.update({
        Device.status: status,
        Device.updated_at: datetime.now(),
    }).where(
        Device.id == device_id
    ).run()
    
async def delete_device_by_in_id_db(device_id):
    await Device.delete().where(
        Device.id == device_id
    ).run()