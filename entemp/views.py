from django.shortcuts import render
from django.http import HttpResponse
from html.parser import HTMLParser
import pandas as pd
import requests
import math


def entemp_view(request):

# Column List ['Year' 'Month' 'Day' 'Maximum T' 'Minimum T' 'Precipitation' 'Snow' 'Snow Depth']

    #Let's not leave this as just a bad redirect.
    source_url = 'https://psl.noaa.gov/boulder/data.daily.html'
    html = requests.get(source_url)
    # This is currently molasses, my guess being that's it's due to lxml vs. html5lib
    # under the hood. 
    #TODO: Update below to just use lxml and pass that to pandas.
    dfs = pd.read_html(io=html.text, match='2021\s+')
    # Current read_html setup is creating duplicate dataframes for each month
    # Hence the isnan check.
    good_frames = [frame for frame in dfs if not math.isnan(frame.iat[0,1])] 
    full_frame = pd.concat(good_frames, ignore_index=True)
    #Really interested in what's happening with the indexing here.

    #This is the full data set but it includes the Leap Day which I'm going to assume we don't want.
    leap_ind = full_frame[((full_frame['Month'] == 2) &( full_frame['Day'] == 29))].index
    #Welp. Hate everything about this.
    df = full_frame.drop(leap_ind)

    print('Index', leap_ind)
    #Add average temp column.

    #Pull Standard Deviation
    # Add average columns
    #print(full_frame.columns.values)
    return HttpResponse(df.to_string())
