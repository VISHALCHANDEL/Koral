import uuid
from .models import Device

class DeviceMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        device_id = request.COOKIES.get("device_id")

        if device_id:
            request.device_id = device_id
        else:
            device = Device.objects.create()
            request.device_id = str(device.id)
            request.new_device = True

        response = self.get_response(request)

        if getattr(request, "new_device", False):
            response.set_cookie("device_id", request.device_id, max_age=31536000)

        return response