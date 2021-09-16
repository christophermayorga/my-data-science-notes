import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def prep_dosage_data(df):
    '''
    This function will perform all the necessary cleaning on the original dataframe.
    '''
    # Create new columns that convert minutes to hours
    df['Monthly_Dosage_Hours'] = df.Monthly_Dosage_Minutes / 60
    df['Hours_Cumulative_Monthly_Dosage'] = df.Cumulative_Monthly_Dosage / 60
    
    # Turn Month_Year into a datetime object
    df.Month_Year = pd.to_datetime(df.Month_Year)
    
    