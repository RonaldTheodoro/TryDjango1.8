from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render
from .forms import SignUpForm, ContactForm


def home(request):
    title = 'Welcome'

    form = SignUpForm(request.POST or None)
    context = {
        'title': title,
        'form': form
    }
    if form.is_valid():
        form.save()
        context = {
            'title': 'Thank you',
        }
    return render(request, 'home.html', context)


def contact(request):
    form = ContactForm(request.POST or None)

    if form.is_valid():
        form_email = form.cleaned_data.get('email')
        form_message = form.cleaned_data.get('message')
        form_full_name = form.cleaned_data.get('full_name')

        subject = 'Site contact forn'
        from_email = settings.EMAIL_USER
        to_email = [from_email, form_email]
        contact_message = 'Name: {} Message: {} Via: {}'.format(
                form_full_name,
                form_message,
                form_email
        )

        send_mail(
                subject,
                contact_message,
                from_email,
                to_email,
                fail_silently=True
        )
    context = {
        'form': form,
        'title': 'Contato'
    }
    return render(request, 'form.html', context)
