#!/usr/bin/env python
# coding: utf-8

# ## The forecasting model: Facebook’s Prophet
# The most commonly used models for forecasting predictions are the autoregressive models. Briefly, the autoregressive model specifies that the output variable depends linearly on its own previous values and on a stochastic term (an imperfectly predictable term).
# 
# Recently, in an attempt to develop a model that could capture seasonality in time-series data, Facebook developed the famous Prophet model that is publicly available for everyone. We will use this state-of-the-art model: the Prophet model. Prophet is able to capture daily, weekly and yearly seasonality along with holiday effects, by implementing additive regression models.
# The mathematical equation behind the Prophet model is defined as:
# 
# **y(t) = g(t) + s(t) + h(t) + e(t)**
# 
# with, g(t) representing the trend. Prophet uses a piecewise linear model for trend forecasting.
# 
# s(t) represents periodic changes (weekly, monthly, yearly).
# 
# h(t) represents the effects of holidays (recall: Holidays impact businesses).
# 
# e(t) is the error term.
# 
# The Prophet model fitting procedure is usually very fast (even for thousands of observations) and it does not require any data pre-processing. It deals also with missing data and outliers.

# # TESLA

# In[ ]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# Load the dataset using pandas
data = pd.read_csv("../input/tesla-share/TSLA (1).csv") 
data.head()


# In[ ]:


data.describe()


# In[ ]:


# Select only the important features i.e. the date and price
data = data[["Date","Close"]] # select Date and Price
# Rename the features: These names are NEEDED for the model fitting
data = data.rename(columns = {"Date":"ds","Close":"y"}) #renaming the columns of the dataset
data.head()


# In[ ]:


get_ipython().system('pip install fbprophet')


# In[ ]:


from fbprophet import Prophet
m = Prophet(daily_seasonality = True) # the Prophet class (model)
m.fit(data) # fit the model using all data


# In[ ]:


future = m.make_future_dataframe(periods=365) #we need to specify the number of days in future
prediction = m.predict(future)
m.plot(prediction)
plt.title("Prediction of the Tesla Stock Price using the Prophet")
plt.xlabel("Date")
plt.ylabel("Close Stock Price")
plt.show()


# In[ ]:


m.plot_components(prediction)
plt.show()


# # TCS

# In[ ]:


# Load the dataset using pandas
data = pd.read_csv("../input/tcs-share/TCS.NS (1).csv") 
data.head()


# In[ ]:


data.describe()


# In[ ]:


# Select only the important features i.e. the date and price
data = data[["Date","Close"]] # select Date and Price
# Rename the features: These names are NEEDED for the model fitting
data = data.rename(columns = {"Date":"ds","Close":"y"}) #renaming the columns of the dataset
data.head()


# In[ ]:


from fbprophet import Prophet
m = Prophet(daily_seasonality = True) # the Prophet class (model)
m.fit(data) # fit the model using all data


# In[ ]:


future = m.make_future_dataframe(periods=365) #we need to specify the number of days in future
prediction = m.predict(future)
m.plot(prediction)
plt.title("Prediction of the TCS Stock Price using the Prophet")
plt.xlabel("Date")
plt.ylabel("Close Stock Price")
plt.show()


# In[ ]:


m.plot_components(prediction)
plt.show()


# # S&P Global

# In[ ]:


# Load the dataset using pandas
data = pd.read_csv("../input/sp-global/GSPC.csv") 
data.head()


# In[ ]:


data.describe()


# In[ ]:


# Select only the important features i.e. the date and price
data = data[["Date","Close"]] # select Date and Price
# Rename the features: These names are NEEDED for the model fitting
data = data.rename(columns = {"Date":"ds","Close":"y"}) #renaming the columns of the dataset
data.head()


# In[ ]:


from fbprophet import Prophet
m = Prophet(daily_seasonality = True) # the Prophet class (model)
m.fit(data) # fit the model using all data


# In[ ]:


future = m.make_future_dataframe(periods=365) #we need to specify the number of days in future
prediction = m.predict(future)
m.plot(prediction)
plt.title("Prediction of the S&P Global Stock Price using the Prophet")
plt.xlabel("Date")
plt.ylabel("Close Stock Price")
plt.show()


# In[ ]:


m.plot_components(prediction)
plt.show()


# # BitCoin

# In[ ]:


# Load the dataset using pandas
data = pd.read_csv("../input/bitcoin/BTC-USD.csv") 
data.head()


# In[ ]:


data.describe()


# In[ ]:


# Select only the important features i.e. the date and price
data = data[["Date","Close"]] # select Date and Price
# Rename the features: These names are NEEDED for the model fitting
data = data.rename(columns = {"Date":"ds","Close":"y"}) #renaming the columns of the dataset
data.head()


# In[ ]:


from fbprophet import Prophet
m = Prophet(daily_seasonality = True) # the Prophet class (model)
m.fit(data) # fit the model using all data


# In[ ]:


future = m.make_future_dataframe(periods=365) #we need to specify the number of days in future
prediction = m.predict(future)
m.plot(prediction)
plt.title("Prediction of the Bitcoin Stock Price using the Prophet")
plt.xlabel("Date")
plt.ylabel("Close Stock Price")
plt.show()


# In[ ]:


m.plot_components(prediction)
plt.show()

