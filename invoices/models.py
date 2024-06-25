from django.db import models

from profiles.models import Profile
from receivers.models import Receiver


class Invoice(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    receiver = models.ForeignKey(Receiver, on_delete=models.CASCADE)
    number = models.CharField(max_length=100)
    is_closed = models.BooleanField(default=False)
    complition_date = models.DateField()
    issue_date = models.DateField()
    payment_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.pk} Invoice number: {self.number}"
