#!/usr/bin/python3

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

def autohist(df, col_name, save_dir):
    
    if df[col_name].dtype != 'object':
        num_data = len(df[col_name])
        num_data_sq = round(np.sqrt(num_data), 1)
        min_col = df[col_name].min()
        max_col = df[col_name].max()
        bin_width = (max_col - min_col) / num_data_sq

        num_bins=np.arange(min_col, max_col + bin_width, bin_width)
    else:
        num_bins = len(df[col_name].unique())

    plt.hist(df[col_name], bins=num_bins, edgecolor='black', linewidth=0.5)
    plt.title(f"Histogram for '{col_name}'")
    plt.ylabel('Frequency')
    plt.xlabel(col_name)
    #plt.show()
    plt.savefig(f'{save_dir}/{col_name}_hist.png', bbox_inches='tight')
    plt.close()

def auto_bar(df, x_var, y_var, save_dir):
    ax = sns.countplot(data=df, x=x_var, hue=y_var)
    plt.axhline(0, color='black', linewidth=1)  
    plt.title(f'{x_var.capitalize()} by {y_var.capitalize()}', fontsize=14)
    ax.set_xlabel(x_var.capitalize(), fontsize=12, labelpad=20)
    ax.set_ylabel('Count', fontsize=12, labelpad=10)
    plt.savefig(f'{save_dir}/{x_var}_{y_var}_barplot.png', bbox_inches='tight')
    plt.clf()

def auto_qq(df, col_name, save_dir):
    import statsmodels.api as sm
    import matplotlib.pyplot as plt

    sm.qqplot(df[col_name])

    #plt.show()
    plt.savefig(f'{save_dir}/{col_name}_qq.png', bbox_inches='tight')
    plt.close()

def auto_box_whisker(df, colname):
    import matplotlib.pyplot as plt
    
    fig = plt.figure(figsize =(4, 3))
    ax = fig.add_subplot()
    ax.boxplot(df[colname])
    ax.set_ylabel('value')
    ax.set_xlabel(colname)
    ax.set_title(f'Box Plot for {colname}')
    plt.show()
