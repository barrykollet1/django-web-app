from django.core.mail import send_mail
from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from listings.forms import ContactUsForm, BandForm, ListingForm


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


def band_create(request):
    if request.method == 'POST':
        form = BandForm(request.POST)
        if form.is_valid():
            # créer une nouvelle « Band » et la sauvegarder dans la db
            band = form.save()
            # redirige vers la page de détail du groupe que nous venons de créer
            # nous pouvons fournir les arguments du motif url comme arguments à la fonction de redirection
            return redirect('band-detail', band.id)

    else:
        form = BandForm()

    return render(request, 'listings/band_create.html', {'form': form})


def about(request):
    return render(request, 'listings/aboutus.html')


def listing_list(request):
    liste = Listing.objects.all()
    return render(request, 'listings/listing_list.html', {"liste": liste})


def listing_detail(request, id_list):
    elem = Listing.objects.get(id=id_list)
    return render(request, 'listings/listing_detail.html', {"list_elem": elem})


def listing_create(request):
    if request.method == 'POST':
        form = ListingForm(request.POST)
        if form.is_valid():
            listing = form.save()
            return redirect('listing-detail', listing.id)
    else:
        form = ListingForm()
    return render(request, 'listings/listing_create.html', {'form': form})


def contact(request):
    # print("La methode de requête est : ", request.method)
    # print("Les données post sont : ", request.POST)
    if request.method == 'POST':
        # créer une instance de notre formulaire et le remplir avec les données POST
        form = ContactUsForm(request.POST)

        if form.is_valid():
            send_mail(
                subject=f'Message from {form.cleaned_data["name"] or "anonyme"} via MerchEx Contact Us form',
                message=form.cleaned_data['message'],
                from_email=form.cleaned_data['email'],
                recipient_list=['admin@merchex.xyz']
            )
            return redirect('email-sent')
    else:
        # ceci doit être une requête GET, donc créer un formulaire vide
        form = ContactUsForm()

    return render(request, 'listings/contact.html', {'form': form})


def sendmail(request):
    return render(request, 'listings/sendmail.html')
