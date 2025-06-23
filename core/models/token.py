from django.db import models
from django.utils.timezone import now
from datetime import timedelta

class IXAPIToken(models.Model):
    access_token = models.TextField()
    refresh_token = models.TextField()
    expires_at = models.DateTimeField()

    def is_expired(self):
        return now() >= self.expires_at

    def __str__(self):
        return f"Token (expires at {self.expires_at})"
