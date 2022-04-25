from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
from listings.models import Band
from listings.models import Listing


def hello(request):
    bands = Band.objects.all()
    return HttpResponse(f"""
        <html>
            <head><title>Merchex</title><head>
            <body>
                <h1>Hello Django !</h1>
                <p>Mes groupes préférés sont :<p>
                <ul>
                    <li>{bands[0].name}</li>
                    <li>{bands[1].name}</li>
                    <li>{bands[2].name}</li>
                </ul>
            </body>
        </html>
    """)


def about(request):
    return HttpResponse('<h1>À propos</h1> <p>Nous adorons merch !</p>'
                        '<input type=button value=Valider class=btn></input>')


def listings(request):
    liste = Listing.objects.all()
    return HttpResponse(f"""
    <h1>Liste des produits</h1>
    <ul>
        <li>{liste[0].title}</li>
        <li>{liste[1].title}</li>
        <li>{liste[2].title}</li>
    </ul>
    
    """)


def contact(request):
    return HttpResponse('<h1>Pour nous contacter</h1> <p>Nous sommes à votre disposition !</p>')
