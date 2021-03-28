from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import Contact
from django.contrib import messages


# Create your views here.
def home(request):
    return render(request, 'home/index.html')


def about(request):
    return render(request, 'home/about.html')


def contact(request):
    CONTACT_SUBMITTED = False  # Initializing CONTACT_SUBMITTED with False
    if request.method == 'POST':  # Ensuring to get name, email... only when there is POST method
        name = request.POST['name']
        email = request.POST['email']
        phone_number = request.POST['phoneNumber']
        issue = request.POST['issue']
        # | Creating a object of Contact model |
        contact = Contact(name=name, email=email, phone_number=phone_number, issue_message=issue)
        contact.save()  # Saving information into database
        CONTACT_SUBMITTED = True  # Changing CONTACT_SUBMITTED to True to get Thank you Message

    # Rendering contact.html with context contact_status : CONTACT_SUBMITTED
    return render(request, 'home/contact.html', {"contact_status": CONTACT_SUBMITTED})
