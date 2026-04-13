from django.db import models

class UserData(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    sentence = models.TextField()

    typing_speed = models.FloatField(null=True, blank=True)
    mouse_speed = models.FloatField(null=True, blank=True)

    ip_address = models.GenericIPAddressField(null=True, blank=True)
    device_info = models.TextField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name