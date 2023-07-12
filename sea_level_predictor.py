import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Read data from file
    df=pd.read_csv('epa-sea-level.csv')
    

    # Create scatter plot
    df.plot.scatter(x='Year', y='CSIRO Adjusted Sea Level')

    # Create first line of best fit
    res = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    time= np.arange(df['Year'].min(), 2050, 1)
    inter= time*res.slope + res.intercept
    plt.plot(time, inter)

    # Create second line of best fit
    df2000=df[df['Year']>=2000]
    res2= linregress(df2000['Year'], df2000['CSIRO Adjusted Sea Level'])
    time2= np.arange(2000, 2050, 1)
    inter2= time2*res2.slope + res2.intercept
    plt.plot(time2, inter2)

    # Add labels and title
    plt.xlabel='Year'
    plt.ylabel='Sea level (inches)'
    plt.title='Rise in Sea Level'
    
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()