# Progammer - Umar Chaudhry
# I attest that all the work done in this program has been done following the policies of the syllabus and project description.
"Create functions to analyze 'videogames.csv' for possible correlations of video game sales and other factors"

import pandas as pd
import numpy as np

def highestsales(year):
    "return dataframe with data of the highest global selling video game of a given year"
    # 'videogames.csv' has data from 1980-2016
    year_range = np.arange(1980,2017)
    year = int(year)
    if year in year_range:
        df = pd.read_csv('videogames.csv')
        gameyear = df[df['Year_of_Release']==year]
        data = gameyear[gameyear["Global_Sales"] == gameyear["Global_Sales"].max()]
        return data
    else:
        raise ValueError("Please enter a year between 1980-2016 as an argument")

def highestgenres():
    "return dataframe with sales data of video games for respective genres"
    df = pd.read_csv('videogames.csv')
    genres = df.groupby('Genre')
    salesdata = genres.sum()
    return salesdata[['NA_Sales','EU_Sales','JP_Sales','Other_Sales','Global_Sales']]

def highestplatforms():
    "return dataframe with sales data of video games for respective platforms/consoles"
    df = pd.read_csv('videogames.csv')
    platforms = df.groupby('Platform')
    data = platforms.sum()
    return data[['NA_Sales','EU_Sales','JP_Sales','Other_Sales','Global_Sales']]

def highestESRB():
    "return dataframe with sales data of video games for respective ESRB ratings"
    df = pd.read_csv('videogames.csv')
    ratings = df.groupby('Rating')
    data = ratings.sum()
    return data[['NA_Sales','EU_Sales','JP_Sales','Other_Sales','Global_Sales']]

def highestdeveloper():
    "return dataframe with sales data of video games for respective developer organizations"
    df = pd.read_csv('videogames.csv')
    developers = df.groupby('Developer')
    data = developers.sum()
    # enable code below to get the top 106 highest global selling video game developers instead of having default 1696 entries
    # data = data[data['Global_Sales'] > 12] 
    return data[['NA_Sales','EU_Sales','JP_Sales','Other_Sales','Global_Sales']]