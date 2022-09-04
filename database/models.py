from django.db import models

# Create your models here.

class detail(models.Model):
    key = models.CharField(max_length=30)
    value = models.TextField(blank=True, default=None, null=True, editable=True)
    def __str__(self) -> str:
        return self.key