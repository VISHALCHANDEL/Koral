from .models import Device
from .qr import generate_qr

def get_device_qr(device_id):
    device = Device.objects.get(id=device_id)
    return generate_qr(device.id)