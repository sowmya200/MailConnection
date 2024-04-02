# management/commands/process_incoming_emails.py
from django.core.management.base import BaseCommand
from django_mailbox.models import Mailbox
from BackendApp.models import IncomingMail

class Command(BaseCommand):
    help = 'Process incoming emails'

    def handle(self, *args, **options):
        mailbox = Mailbox.objects.first()
        if not mailbox:
            self.stdout.write(self.style.WARNING('No mailbox configuration found.'))
            choice = input('Do you want to configure a mailbox? (yes/no): ')
            if choice.lower() == 'yes':
                # Code to configure mailbox goes here
                self.stdout.write(self.style.SUCCESS('Mailbox configured successfully.'))
                mailbox = Mailbox.objects.first()  # Attempt to retrieve mailbox again
            else:
                self.stdout.write(self.style.ERROR('Exiting without processing emails.'))
                return
        
        if mailbox:
            messages = mailbox.get_new_mail()
            for message in messages:
                IncomingMail.objects.create(
                    subject=message.subject,
                    sender=message.from_address,
                    body=message.text,
                )
            self.stdout.write(self.style.SUCCESS('Successfully processed incoming emails.'))