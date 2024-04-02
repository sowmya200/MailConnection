#from django.db import models

# Create your models here.
# models.py
from django.db import models

class IncomingMail(models.Model):
    subject = models.CharField(max_length=255)
    sender = models.EmailField()
    body = models.TextField()
    received_at = models.DateTimeField(auto_now_add=True)
