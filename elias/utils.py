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


# # Sample DataFrame (replace this with your actual DataFrame)
# data = {'value_column': [1, 2, 2, 2, 3, 3, 3, 4, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 7, 8, 8]}
# frame = pd.DataFrame(data)
# print(remove_constant_values(frame, "value_column", 3))
