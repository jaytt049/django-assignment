from django.db import models
from django.contrib.auth.models import User

class Lead(models.Model):
    STATUS_CHOICE = [
        ('new', 'New'),
        ('contacted', 'Contacted'),
        ('closed', 'Closed'),
    ]
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)

    status = models.CharField(max_length=20, choices=STATUS_CHOICE, default='new')

    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    