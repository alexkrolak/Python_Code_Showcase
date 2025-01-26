

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math

def view_cat_uniques(df, columns):
    """
    Prints the value counts (distribution) of each column in columns, sorted by descending frequency.
    Also identifies if any column appears to have duplicates (particularly useful for ID columns).

    Parameters:
    -----------
    df : pandas.DataFrame
        The DataFrame to analyze.
    columns : list of str
        The columns in df for which to print value counts.
    """
    for col in columns:
        print(f"\n=== Distribution of '{col}' ===")
        distribution = (
            df[col]
            .value_counts(dropna=False)  # include NaN in counts
            .reset_index(name='count')
            .sort_values('count', ascending=False)
        )
        print(distribution.to_string(index=False))
        
# Creates a histogram for any/all numeric columns        
def plot_histogram(df):
    """
    Detects numeric columns in df, then plots histograms for each column.
    Displays them in rows of at most 3 plots each.
    """
    # Select numeric columns
    numeric_cols = df.select_dtypes(include=["number"]).columns.tolist()
    if not numeric_cols:
        print("No numeric columns found for histogram.")
        return
    
    # Calculate how many rows of subplots we need
    num_cols = len(numeric_cols)
    cols_per_row = 3
    rows = math.ceil(num_cols / cols_per_row)
    
    fig, axes = plt.subplots(rows, cols_per_row, figsize=(5*cols_per_row, 4*rows))
    axes = axes.flatten()  # to iterate over
    
    for i, col in enumerate(numeric_cols):
        ax = axes[i]
        # Drop NaN values to avoid issues with .hist()
        data = df[col].dropna()
        ax.hist(data, bins=20, color='skyblue', edgecolor='black')
        ax.set_title(f"{col} (n={len(data)})")
    
    # If there are unused subplots, hide them
    for j in range(i+1, rows * cols_per_row):
        fig.delaxes(axes[j])
    
    plt.tight_layout()
    plt.show()

# Creates a barplot for each categorical variable
def plot_bar(df, max_unique=50):
    """
    Detects categorical columns (including datetime columns with <= max_unique unique values).
    Plots bar plots of frequencies for columns with <= max_unique unique categories.
    Ignores columns with more than max_unique categories.
    
    Parameters:
    -----------
    df : pd.DataFrame
        The dataframe to analyze.
    max_unique : int
        Maximum number of unique values in a column to qualify for bar plot.
    """
    # We'll consider 'object' or 'category' types as categorical.
    # Also consider datetime columns with small cardinality as categorical.
    
    # Identify candidate columns
    cat_cols = []
    for col in df.columns:
        col_type = df[col].dtype
        
        # If it's datetime, check unique count
        if pd.api.types.is_datetime64_any_dtype(col_type):
            # dropna() before checking unique
            unique_vals = df[col].dropna().unique()
            if len(unique_vals) <= max_unique:
                cat_cols.append(col)
        
        # If it's string/object or category
        elif pd.api.types.is_string_dtype(col_type) or pd.api.types.is_categorical_dtype(col_type):
            unique_vals = df[col].dropna().unique()
            if len(unique_vals) <= max_unique:
                cat_cols.append(col)
    
    if not cat_cols:
        print("No suitable categorical columns found for bar plots.")
        return
    
    # Now plot each cat col in rows of 3
    num_cols = len(cat_cols)
    cols_per_row = 3
    rows = math.ceil(num_cols / cols_per_row)
    
    fig, axes = plt.subplots(rows, cols_per_row, figsize=(5*cols_per_row, 4*rows))
    axes = axes.flatten()
    
    for i, col in enumerate(cat_cols):
        ax = axes[i]
        data = df[col].dropna()  # ignore NaN for frequency counts
        counts = data.value_counts()
        
        # plot bar
        counts.plot.bar(ax=ax, color='orange', edgecolor='black')
        ax.set_title(f"{col} (unique={counts.shape[0]})")
        ax.set_xlabel(col)
        ax.set_ylabel("Frequency")
    
    # Hide unused subplots if any
    for j in range(i+1, rows * cols_per_row):
        fig.delaxes(axes[j])
    
    plt.tight_layout()
    plt.show()
