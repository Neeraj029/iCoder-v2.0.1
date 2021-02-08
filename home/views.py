from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'home/index.html')

def about(request):
    return render(request, 'home/about.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone_number = request.POST['phoneNumber']
        issue = request.POST['issue']
    CONTACT_SUBMITTED = True

    return render(request, 'home/contact.html', {"contact_status" : CONTACT_SUBMITTED})
