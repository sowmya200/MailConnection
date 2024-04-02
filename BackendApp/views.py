
from django.shortcuts import render
from django.core.management import call_command

def process_incoming_emails_view(request):
    # Call the management command to process incoming emails
    call_command('process_incoming_emails')
    return render(request, 'process_emails_success.html')
