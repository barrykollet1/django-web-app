from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
from listings.models import Band
from listings.models import Listing


def hello(request):
    bands = Band.objects.all()
    return render(request, 'listings/hello.html', {'bands': bands})


def about(request):
    return render(request, 'listings/aboutus.html')


def listings(request):
    liste = Listing.objects.all()
    return render(request, 'listings/listing.html', {"liste": liste})


def contact(request):
    return render(request, 'listings/contactus.html')
