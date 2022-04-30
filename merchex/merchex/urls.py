"""merchex URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from listings import views

urlpatterns = [
    # path('', views.hello),
    path('admin/', admin.site.urls),

    path('bands/', views.band_list, name='band-list'),
    path('bands/<int:band_id>/', views.band_detail, name='band-detail'),
    path('bands/add', views.band_create, name='band-creation'),
    path('bands/<int:band_id>/change/', views.band_update, name='band-update'),

    path('listing/', views.listing_list, name='listing-list'),
    path('listing/<int:id_list>/', views.listing_detail, name='listing-detail'),
    path('listing/add', views.listing_create, name='listing-creation'),
    path('listing/<int:id_list>/change/', views.listing_update, name='listing-update'),

    path('about-us/', views.about, name='about-us'),
    path('contact-us/', views.contact, name='contact-us'),
    path('send-main/', views.sendmail, name='email-sent'),

]
