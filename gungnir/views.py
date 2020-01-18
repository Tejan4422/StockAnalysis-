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
from .models import Cal
from sklearn.ensemble import RandomForestRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.svm import SVR


def homepage(request):

    c = 'Tejan'
    return render(request, 'home.html', {'result': c})


def predict(request):

    company = request.POST['companyname']
    sd = request.POST['startdate']
    ed = request.POST['enddate']
    print(company,sd,ed)

    dfYahoo = dr.data.get_data_yahoo(company, sd, ed)
    dfYahoo['Date'] = dfYahoo.index


    close = []
    open1 = []
    high = []
    low = []
    date = []
    ydate = dfYahoo.iloc[:,6].values
    Xdate = pd.to_datetime(ydate, dayfirst = True)

    for i in Xdate:
        c = ''
        c = c + str(i.day) + str(i.month)
        date.append(c)

    #copying length of date to date1
    num = len(date)
    date1 = list(range(1,num+1))
    #converting date to int format
    date = [int(i) for i in date]
    date = np.reshape(date, (len(date), 1))
    date1 = [int(i) for i in date1]
    date1 = np.reshape(date1, (len(date1), 1))

    for index, row in dfYahoo.iterrows():
        high.append(float(row["High"]))
        close.append(float(row["Close"]))
        low.append(float(row["Low"]))
        open1.append(float(row["Open"]))


    print(dfYahoo)
    print(date)
    print(date1)

    randomlow = RandomForestRegressor(n_estimators = 1000)
    randomlow.fit(date1, low)
    random_low = randomlow.predict([[num+1]])
    decisionlow = DecisionTreeRegressor()
    decisionlow.fit(date1, low)
    decision_low = decisionlow.predict([[num+1]])
    svrlow = SVR(kernel = 'rbf', C = 1e3, gamma = 0.1)
    svrlow.fit(date1, low)
    svr_low = svrlow.predict([[num+1]])

    randomhigh = RandomForestRegressor(n_estimators = 1000)
    randomhigh.fit(date1, high)
    random_high = randomhigh.predict([[num+1]])
    decisionhigh = DecisionTreeRegressor()
    decisionhigh.fit(date1, high)
    decision_high = decisionhigh.predict([[num+1]])
    svrhigh = SVR(kernel = 'rbf', C = 1e3, gamma = 0.1)
    svrhigh.fit(date1, high)
    svr_high = svrhigh.predict([[num+1]])

    randomclose = RandomForestRegressor(n_estimators = 1000)
    randomclose.fit(date1, close)
    random_close = randomclose.predict([[num+1]])
    decisionclose = DecisionTreeRegressor()
    decisionclose.fit(date1, close)
    decision_close = decisionclose.predict([[num+1]])
    svrclose = SVR(kernel = 'rbf', C = 1e3, gamma = 0.1)
    svrclose.fit(date1, close)
    svr_close = svrclose.predict([[num+1]])

    print(num+1)
    print(random_low)
    print(decision_low)
    print(svr_low)
    print(random_high)
    print(decision_high)
    print(svr_high)
    print(random_close)
    print(decision_close)
    print(svr_close)

    c = 'Tejan'
    return render(request, 'predict.html', {'rlow': random_low,
    'dlow' : decision_low, 'slow' : svr_low, 'rhigh': random_high,
    'dhigh' : decision_high, 'shigh' : svr_high, 'rclose': random_close,
    'dclose' : decision_close, 'sclose' : svr_close})

def visualize(request):
    company = request.POST['companyname']
    sd = request.POST['startdate']
    ed = request.POST['enddate']
    print(company,sd,ed)

    df = dr.data.get_data_yahoo(company, sd, ed)
    print(df)


    df = df.rename(index=str, columns={"index": "date", "1. open": "open", "2. high": "high", "3. low": "low", "4. close": "close","5. volume":"volume"})
    print(df)
    df = df.reset_index()
    print(df)

    df['Date'] = pd.to_datetime(df['Date'])

    print(df)

    df = df.sort_values(by=['Date'])
    #Changing the datatype
    df.Open = df.Open.astype(float)
    df.Close = df.Close.astype(float)
    df.High = df.High.astype(float)
    df.Low = df.Low.astype(float)
    df.Volume = df.Volume.astype(int)
    #check the data
    df.head()
    #Check the datatype
    df.info()

    #Visalization
    inc = df.Close > df.Open
    dec = df.Open > df.Close
    w = 12*60*60*1000 # half day in ms
    TOOLS = "pan,wheel_zoom,box_zoom,reset,save"
    title = company + ' Chart'
    p = figure(x_axis_type="datetime", tools=TOOLS, plot_width=1000, title = title)
    p.xaxis.major_label_orientation = 3.14/4
    p.grid.grid_line_alpha=0.3
    p.segment(df.Date, df.High, df.Date, df.Low, color="black")
    p.vbar(df.Date[inc], w, df.Open[inc], df.Close[inc], fill_color="#D5E1DD", line_color="black")
    p.vbar(df.Date[dec], w, df.Open[dec], df.Close[dec], fill_color="#F2583E", line_color="black")
    #Store as a HTML file
    output_file("stock_information.html", title="candlestick.py example")
    # Display in browser
    show(p)

    return render(request, 'home.html')
