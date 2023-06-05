from django.http import HttpResponse
from django.shortcuts import render
from listings.models import Band


def hello(request):
    bands = Band.objects.all()
    return render(request, 'listings/hello.html', context={'bands':bands})


def about(request):
    return HttpResponse('<h1>About us</h1> <p>We love merch!</p>')