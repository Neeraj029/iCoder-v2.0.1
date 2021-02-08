from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import Contact

# Create your views here.
def home(request):
    return render(request, 'home/index.html')

def about(request):
    return render(request, 'home/about.html')

def contact(request):
    CONTACT_SUBMITTED = False
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone_number = request.POST['phoneNumber']
        issue = request.POST['issue']
        contact = Contact(name = name, email=email, phone_number=phone_number, issue_message=issue)
        contact.save()
        CONTACT_SUBMITTED = True


    return render(request, 'home/contact.html', {"contact_status" : CONTACT_SUBMITTED})
