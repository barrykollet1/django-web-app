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


def band_update(request, band_id):
    band = Band.objects.get(id=band_id)

    if request.method == 'POST':
        form = BandForm(request.POST, instance=band)
        # mettre à jour le groupe existant dans la base de données
        form.save()
        # rediriger vers la page détaillée du groupe que nous venons de mettre à jour
        return redirect('band-detail', band.id)
    else:
        form = BandForm(instance=band)

    return render(request, 'listings/band_update.html', {'form': form})


def band_delete(request, band_id):
    band = Band.objects.get(id=band_id)    # nécessaire pour GET et pour POST

    if request.method == 'POST':
        # supprimer le groupe de la base de données
        band.delete()
        # rediriger vers la liste des groupes
        return redirect('band-list')

    # pas besoin de « else » ici. Si c'est une demande GET, continuez simplement

    return render(request, 'listings/band_delete.html', {'band': band})


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


def listing_update(request, id_list):
    listing = Listing.objects.get(id=id_list)

    if request.method == 'POST':
        form = ListingForm(request.POST, instance=listing)
        # mettre à jour le groupe existant dans la base de données
        form.save()
        # rediriger vers la page détaillée du groupe que nous venons de mettre à jour
        return redirect('listing-detail', listing.id)
    else:
        form = ListingForm(instance=listing)

    return render(request, 'listings/listing_update.html', {'form': form})


def listing_delete(request, id_list):
    listing = Listing.objects.get(id=id_list)    # nécessaire pour GET et pour POST

    if request.method == 'POST':
        # supprimer le groupe de la base de données
        listing.delete()
        # rediriger vers la liste des groupes
        return redirect('listing-list')

    # pas besoin de « else » ici. Si c'est une demande GET, continuez simplement

    return render(request, 'listings/listing_delete.html', {'listing': listing})



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
