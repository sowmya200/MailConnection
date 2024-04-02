# admin.py in BackendApp

from django.contrib import admin
from .models import IncomingMail

admin.site.register(IncomingMail)
