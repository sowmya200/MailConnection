from django.test import TestCase
from django.core.mail import send_mail

send_mail(
    'Subject here',
    'Here is the message.',
    'sowmyakumaravel2002@gmail.com',
    ['sowmyakumaravel2024@gmail.com.com'],
    fail_silently=False,
)

# Create your tests here.
