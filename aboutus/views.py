from django.shortcuts import render

from .models import Aboutus

# Create your views here.
def aboutus(request):

    aboutus = Aboutus.objects




    return render(request, 'aboutus/about.html', {'aboutus' : aboutus})
