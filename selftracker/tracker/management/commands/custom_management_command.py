from django.core.management.base import BaseCommand
from tracker.models import ActionPlanner
from datetime import date
from django.core.mail import EmailMessage

class Command(BaseCommand):
    help = 'Sends notifications on remainders'
    
    def handle(self, *args, **kwargs):
        today = date.today()
        remainders = ActionPlanner.objects.filter(date__year=today.year, date__month=today.month, date__day=today.day)
        if remainders:
            for remainder in remainders:
                message = "Hi "+remainder.user.username+",\n\n There is a gentle remainder on "+ remainder.title + ".\n\n The detail description of remainder is \"" +remainder.description +"\".\n\nHave a nice day! Keep Smiling!\n\nThanks and Regards,\nSelf Tacker Team"
                email = EmailMessage()
                email.subject = 'Remainder'
                email.body = message
                email.to = [remainder.user.email]
                email.send(fail_silently=False)
            print("Reminder is sent")
        else:
            print("There is no reminder to send")