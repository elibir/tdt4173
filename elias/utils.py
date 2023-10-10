import matplotlib.pyplot as plt
import pandas as pd


def plot_ts(y, x, start, end, feature, shareX: bool):
    fig, axs = plt.subplots(len(x)+len(y), 1, figsize=(15,10), sharex=shareX)
    i = 0
    for df in y:
        df[(df.index >= start) & (df.index <= end)].resample("H").mean().plot(ax=axs[i])
        i += 1
    
    for df in x:
        df[(df.index >= start) & (df.index <= end)].resample("H").mean()[feature].plot(ax=axs[i], label=feature, color="red")
        axs[i].legend()
        i += 1
  
def quarter_to_hour(df):    
    
    new_df = df.copy()
    
    for i in range(0, len(new_df), 4):
        if i + 4 <= len(new_df):
            mean_values = new_df.iloc[i:i+4].mean()
            new_df.iloc[i] = mean_values
    return new_df
