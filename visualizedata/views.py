from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
import django
import requests
import pandas as pd
from datetime import datetime
import pandas_datareader as dr
from bokeh.plotting import figure, show, output_file
import io
import numpy as np
import pandas_datareader as dr
import csv
import sklearn
import matplotlib as plt
from sklearn.svm import SVR
from sklearn.ensemble import RandomForestRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.svm import SVR


from .models import VisualizeData

# Create your views here.
def visualizeCases(request):

    visualizedata = VisualizeData.objects




    return render(request, 'visualizedata/visualize.html', {'visualizedata' : visualizedata})
