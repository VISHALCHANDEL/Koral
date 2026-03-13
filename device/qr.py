import qrcode
from django.conf import settings
import os

def generate_qr(device_id):
    qr = qrcode.make(device_id)

    path = os.path.join(settings.MEDIA_ROOT, f"{device_id}.png")
    qr.save(path)

    return f"{settings.MEDIA_URL}{device_id}.png"