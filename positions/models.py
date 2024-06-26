from django.db import models

from invoices.models import Invoice


class Position(models.Model):
    title = models.CharField(max_length=240)
    description = models.TextField(blank=True, help_text="Optional info")
    amount = models.FloatField(help_text="Amount in USD")
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
