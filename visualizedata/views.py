from django.shortcuts import render

from .models import VisualizeData

# Create your views here.
def visualizeCases(request):

    visualizedata = VisualizeData.objects

    return render(request, 'visualizedata/visualize.html', {'visualizedata' : visualizedata})
