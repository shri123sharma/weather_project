# myapp/management/commands/send_reminders.py

from django.core.management.base import BaseCommand
from django.core.mail import send_mail
from django.utils import timezone
from hospital_support.models import Event

class Command(BaseCommand):
    help = 'Send email reminders for events happening after three days'

    def handle(self, *args, **options):
        # Get today's date
        today = timezone.now().date()

        # Query events happening after three days
        future_events = Event.objects.filter(date__gte=today + timezone.timedelta(days=3))

        # Send email reminders to users for each event
        for event in future_events:
            subject = f'Reminder: {event.title}'
            message = f'Don\'t forget! {event.title} is happening on {event.date}.'
            send_mail(subject, message, 'sshrikant919@gmail.com', [event.user_email])
            self.stdout.write(self.style.SUCCESS(f'Reminder sent for event: {event.title}'))
