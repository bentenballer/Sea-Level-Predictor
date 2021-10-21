import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    plt.scatter(x=df["Year"],y=df["CSIRO Adjusted Sea Level"])
    
    # Create first line of best fit
    first_extended = np.arange(1880, 2051, 1)
    first = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
    first_line = [first.slope*year + first.intercept for year in first_extended]
    plt.plot(first_extended, first_line, "r")
    
    # Create second line of best fit
    df2= df[df["Year"]>=2000]
    second_extended = np.arange(2000,2051,1)
    second = linregress(df2["Year"], df2["CSIRO Adjusted Sea Level"])
    second_line = [second.slope*year + second.intercept for year in second_extended]
    plt.plot(second_extended, second_line, "g")

    # Add labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()