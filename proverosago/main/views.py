from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def index(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about.html')





def contact(request):
    return render(request, 'main/contact.html')


def information(request):
    return render(request, 'main/information.html')