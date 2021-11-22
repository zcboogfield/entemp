from django.shortcuts import render
from django.http import HttpResponse
from html.parser import HTMLParser
import pandas as pd
import requests
import math


def entemp_view(response):
# Column List ['Year' 'Month' 'Day' 'Maximum T' 'Minimum T' 'Precipitation' 'Snow' 'Snow Depth']

    source_url = 'https://psl.noaa.gov/boulder/data.daily.html'
    html = requests.get(source_url)
    # This is currently molasses, my guess being that's it's due to lxml vs. html5lib
    # under the hood per the Docs: https://tedboy.github.io/pandas/gotchas/gotchas9.html 
    #TODO: Update below to just use lxml and pass that to pandas.
    dfs = pd.read_html(io=html.text, match='2021\s+')

    # Current read_html setup is creating duplicate dataframes for each month
    # Below ensures we just get one DF for each month between Jan and Oct.
    good_frames = [frame for frame in dfs if frame.iat[0,1] in range(1,11)] 
    full_frame = pd.concat(good_frames, ignore_index=True)

    #This is the full data set but it includes the Leap Day which I assume we don't want.
    leap_ind = full_frame[((full_frame['Month'] == 2) &( full_frame['Day'] == 29))].index
    df = full_frame.drop(leap_ind)

    #Add average temp column.
    df['Average Temp'] = (df['Maximum T'] + df['Minimum T']) / 2

    config = {
            'avg_temp': str(df['Average Temp'].mean()),
            'std_temp': str(df['Average Temp'].std()),
            'header': df.columns.values.tolist(),
            'rows': df.iterrows(),
    }

    return render(response,'temp_page.html', {'config': config})
