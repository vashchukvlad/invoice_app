from datetime import datetime
from django.db import models


class Receiver(models.Model):
    """Class for company that receives the invoice"""

    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    website = models.URLField(blank=True)
    created_at = models.DateTimeField(default=datetime.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
