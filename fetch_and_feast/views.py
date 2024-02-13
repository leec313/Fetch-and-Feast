from django.shortcuts import render
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings


def handler404(request, exception=None):
    """ Error Handler 404 - Page Not Found """
    return render(request, "errors/404.html", status=404)


def faq_view(request):
    return render(request, 'faq.html')


def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Send email to admin
        send_mail(
            subject=f'New Contact Form Submission: {subject}',
            message=f'Name: {name}\nEmail: {email}\nMessage: {message}',
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[settings.DEFAULT_FROM_EMAIL],
        )

        # Send email to user
        send_mail(
            subject='Fetch & Feast: Message Received',
            message='Thank you for contacting us! We have received your message and will get back to you soon.', # noqa
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[email],
        )

        messages.success(request, 'We have received your message!')

    return render(request, 'contact.html')
