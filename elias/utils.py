import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


def plot_ts(y: pd.DataFrame, x:pd.DataFrame, start, end, feature, shareX: bool):
    """
    Plots all the y arrays, then all the x arrays.
    """
    fig, axs = plt.subplots(len(x)+len(y), 1, figsize=(15,10), sharex=shareX)
    i = 0
    for df in y:
        df[(df.index >= start) & (df.index <= end)].resample("H").mean().plot(ax=axs[i])
        i += 1
    
    for df in x:
        df[(df.index >= start) & (df.index <= end)].resample("H").mean()[feature].plot(ax=axs[i], label=feature, color="red")
        axs[i].legend()
        i += 1
    
            
def plot_ts1(y: pd.DataFrame, x:pd.DataFrame, start, end, feature, shareX: bool):
    """
    Plots the y and x values directly under each other for each location
    """
    
    if len(x) != len(y):
        print("Error: arrays 'y' and 'x' are different lengths. Please provide equal sized arrays.")
    else:
        fig, axs = plt.subplots(len(x)+len(y), 1, figsize=(15,10), sharex=shareX)
        i = 0
        for df_y, df_x in zip(y, x):
                df_y[(df_y.index >= start) & (df_y.index <= end)].resample("H").mean().plot(ax=axs[i])
                i += 1
                df_x[(df_x.index >= start) & (df_x.index <= end)].resample("H").mean()[feature].plot(ax=axs[i], label=feature, color="red")
                axs[i].legend()
                i += 1
  
  
def quarter_to_hour(df):    
    """
    Unused function. Experimentation with taking the average weather values across an hour yielded
    worse results than not doing it.
    """
    new_df = df.copy()
    
    for i in range(0, len(new_df), 4):
        if i + 4 <= len(new_df):
            mean_values = new_df.iloc[i:i+4].mean()
            new_df.iloc[i] = mean_values
    return new_df


def create_features(df):
    new_df = df.copy()
    new_df['hour'] = new_df.index.hour
    new_df['dayofyear'] = new_df.index.dayofyear
    return new_df


def remove_constant_values(df, column_name, threshold):
    
    new_df = df.copy()

    # Find the consecutive constant rows
    consecutive_constants = new_df.groupby((new_df[column_name] != new_df[column_name].shift()).cumsum()).filter(lambda x: len(x) > threshold)

    # Filter out the consecutive constant rows from the original DataFrame
    filtered_df = new_df[~new_df.index.isin(consecutive_constants.index)]
    
    return filtered_df

def replace_constant_values_with_nan(df, column_name, threshold):
    new_df = df.copy()

    # Find the consecutive constant rows
    consecutive_constants = new_df.groupby((new_df[column_name] != new_df[column_name].shift()).cumsum()).filter(lambda x: len(x) > threshold)

    # Replace constant values with NaN within the original DataFrame
    new_df.loc[new_df.index.isin(consecutive_constants.index), column_name] = np.nan
    
    return new_df




