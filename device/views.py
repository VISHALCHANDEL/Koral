from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .services import get_device_qr

from django.shortcuts import render
from django.http import HttpResponse
from .services import get_device_qr
import qrcode
import io

def dashboard(request):
    qr_url = get_device_qr(request.device_id)
    return render(request, "device/dashboard.html", {"qr_url": qr_url})

def download_qr(request):
    device_id = request.device_id

    qr = qrcode.make(str(device_id))

    buffer = io.BytesIO()
    qr.save(buffer, format="PNG")
    buffer.seek(0)

    response = HttpResponse(buffer, content_type="image/png")
    response['Content-Disposition'] = 'attachment; filename="koral_qr.png"'

    return response