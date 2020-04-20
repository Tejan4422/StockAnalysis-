# StockAnalysis-Stock Market Analysis and Prediction using Machine Learning algorithms. 
##Use it to predict only stock values for the very next dat.
###Overview
*created a website which can predict following
    *HIGHEST values of a particular company
    *LOWEST values of a particular company
    *CLOSING values of a particular company
*Algorithms used:
    *Decision Tree Regression
    *Random Forest Regression
    *Support Vector Regression
*Data taken from ** https://in.finance.yahoo.com/
* Use pandas-datareader package to connect to yahoo server to fetch dataframe

##Resources Used:
**Python: **3.7
**Packages : **pandas, pnadas-datareader, sklearn, numpy, requests, django, matplotlib, seaborn

##Case Studies:
![alt text](https://github.com/Tejan4422/StockAnalysis-/blob/master/Case%20Studies/Fig_AXIS_Low.png "Model Performance")
![alt text](https://github.com/Tejan4422/StockAnalysis-/blob/master/Case%20Studies/Fig_AXIS_High.png "Model Performance")
![alt text](https://github.com/Tejan4422/StockAnalysis-/blob/master/Case%20Studies/Fig_AXIS_Close.png "Model Performance")
![alt text](https://github.com/Tejan4422/StockAnalysis-/blob/master/Case%20Studies/Fig_AXIB_Low.png"Model Performance")
![alt text](https://github.com/Tejan4422/StockAnalysis-/blob/master/Case%20Studies/Fig_ASHOKLEYLAND_Close.png "Model Performance")

##Model Building:
Initiallly, I connected to yahoo server using pandas-datareader package to fetch data of client defined duration(preffered : data of month or more).

Since data fetched is mostly numerical no need to clean data.

I started implementation with Linear Regression which in this case performs below expectations as can be seen in case studies.

After parameter tuning I figured out RandomForest, SVR and Decision Tree performs pretty well

##Production:

In this step I thought of creating an interactive application for end user. After a lot thought I came up with developing website using
django framework.
Screenshots of website
![alt text](https://github.com/Tejan4422/StockAnalysis-/blob/master/screenshots/homepage.png "Homepage")
![alt text](https://github.com/Tejan4422/StockAnalysis-/blob/master/screenshots/prediction.png "Prediction Table")
