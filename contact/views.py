from django.shortcuts import render
from contact.models import Info
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.


def send_message(request):
    info = Info.objects.first()

    if request.method == 'POST':
        subject = request.POST['subject']
        email = request.POST['email']
        message = request.POST['message']
       
        send_mail(
            subject,

            message,
            
            email,

            [settings.EMAIL_HOST_USER],
            
        ) 

    return render(request,'contact/contact.html',{'info':info})