import uuid
from django.db import models

class Device(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    last_active_at = models.DateTimeField(auto_now=True)
    is_blocked = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)
