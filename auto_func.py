#!/usr/bin/python3

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

def cap_colnames(col_name):
    col_name = [word[0].upper() + word[1:] for word in col_name.split()]
    return col_name

def autohist(df, col_name, save_dir):
    import matplotlib.pyplot as plt
    import numpy as np

    df[col_name].replace([np.inf, -np.inf], np.nan, inplace=True)
    
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


def auto_jointgrid(df, x_col, y_col, save_dir):
    from seaborn import JointGrid

    fig = JointGrid(data=df, x=x_col, y=y_col)
    fig.plot_joint(sns.scatterplot, s=100, alpha=.5)
    fig.plot_marginals(sns.histplot, kde=True)
    plt.title(f"{x_col} vs {y_col}")
    plt.ylabel(y_col)
    plt.xlabel(x_col)
    plt.savefig(f'{save_dir}/{x_col}_{y_col}_jointgrid.png', bbox_inches='tight')
    # plt.show()
    plt.close()



# # updated with capitalzie thing, have to reconcile
# def do_boxplot(df, x_col, y_col, save_dir):
#     fig, ax = plt.subplots(figsize=(11.7, 8.27))
#     sns.boxplot(data=df, x=x_col, y=y_col, ax=ax)

#     x_col_formt=x_col.capitalize()
#     y_col_list = [word[0].upper() + word[1:] for word in y_col.split()]
#     y_col_formt = " ".join(y_col_list)
#     ax.set_title(f'{y_col_formt} by {x_col_formt}')
#     ax.set_xlabel(x_col_formt)
#     ax.set_ylabel(y_col_formt)
#     plt.savefig(f'{save_dir}/{x_col}_{y_col}_hist.png', bbox_inches='tight')
#     plt.show()

# def do_hist(df, x_col, y_col, save_dir):
#     ax = sns.histplot(data=df, x=y_col, hue=x_col, multiple='stack')

#     x_col_formt=x_col.capitalize()
#     y_col_list = [word[0].upper() + word[1:] for word in y_col.split()]
#     y_col_formt = " ".join(y_col_list)
#     ax.set_title(f'{y_col_formt} by {x_col_formt}')
#     ax.set_xlabel(x_col_formt)
#     plt.ylabel('Frequency')
#     sns.move_legend(ax, "upper left", bbox_to_anchor=(1, 1))
#     plt.savefig(f'{save_dir}/{x_col}_{y_col}_hist.png', bbox_inches='tight')
#     plt.show()
