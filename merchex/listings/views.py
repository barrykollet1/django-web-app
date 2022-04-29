from django.http import HttpResponse, Http404
from django.shortcuts import render


# Create your views here.
from listings.models import Band
from listings.models import Listing


def band_list(request):
    bands = Band.objects.all()
    return render(request, 'listings/band_list.html', {'bands': bands})


def band_detail(request, band_id):
    try:
        band = Band.objects.get(id=band_id)
    except Band.DoesNotExist:
        raise Http404("No MyModel matches the given query.")

    return render(request, 'listings/band_detail.html', {'band': band})


def about(request):
    return render(request, 'listings/aboutus.html')


def listing_list(request):
    liste = Listing.objects.all()
    return render(request, 'listings/listing_list.html', {"liste": liste})


def listing_detail(request, id_list):
    elem = Listing.objects.get(id=id_list)
    return render(request, 'listings/listing_detail.html', {"list_elem": elem})


def contact(request):
    return render(request, 'listings/contactus.html')
