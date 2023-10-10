import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


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
    # first, take the mean of every hour in the X value dataset, to match the resolution of the y-values.
    for i in range(0, len(df), 4):
        if i + 4 <= len(df):
            mean_values = df.iloc[i:i+4].mean()
            df.iloc[i] = mean_values
