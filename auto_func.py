
def autohist(df, col_name, save_dir):
    import matplotlib.pyplot as plt
    import numpy as np
    
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

def auto_qq(df, col_name, save_dir):
    import statsmodels.api as sm

    sm.qqplot(df[col_name])

    #plt.show()
    plt.savefig(f'{save_dir}/{col_name}_qq.png', bbox_inches='tight')
    plt.close()


