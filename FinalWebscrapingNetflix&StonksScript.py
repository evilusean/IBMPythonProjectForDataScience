# -*- coding: utf-8 -*-
"""
Created on Fri Jul  8 03:06:08 2022

@author: Shawn Temes
"""
#Install modules
#!pip install pandas==1.3.3
#!pip install requests==2.26.0
!mamba install bs4==4.10.0 -y
!mamba install html5lib==1.1 -y
!pip install lxml==4.6.4
#!pip install plotly==5.3.1

#Load Modules
import pandas as pd
import requests
from bs4 import BeautifulSoup

#Get webpage to extract text
url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/netflix_data_webpage.html"
data  = requests.get(url).text

#parse the text into html using beautiful_soup
soup = BeautifulSoup(data, 'html5lib')

#turn the html table into a pandas dataframe
netflix_data = pd.DataFrame(columns=["Date", "Open", "High", "Low", "Close", "Volume"])

# First we isolate the body of the table which contains all the information
# Then we loop through each row and find all the column values for each row
for row in soup.find("tbody").find_all('tr'):
    col = row.find_all("td")
    date = col[0].text
    Open = col[1].text
    high = col[2].text
    low = col[3].text
    close = col[4].text
    adj_close = col[5].text
    volume = col[6].text
    
    # Finally we append the data of each row to the table
    netflix_data = netflix_data.append({"Date":date, "Open":Open, "High":high, "Low":low, "Close":close, "Adj Close":adj_close, "Volume":volume}, ignore_index=True)    

#check data header
netflix_data.head()

#We can also use the pandas read_html function using the url
read_html_pandas_data = pd.read_html(url)

#Or we can convert the BeautifulSoup object to a string
read_html_pandas_data = pd.read_html(str(soup))

#Because there is only one table on the page, we just take the first table in the list returned
netflix_dataframe = read_html_pandas_data[0]
#check data
netflix_dataframe.head()












