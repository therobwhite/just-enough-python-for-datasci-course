"""
Data loading and configuration utilities for video game sales analysis.

This module provides functions for loading data and setting up the analysis environment.
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def setup_display_options() -> None:
    """Configure pandas and matplotlib display options for better output."""
    # Pandas display options
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', 20)
    pd.set_option('display.float_format', '{:.2f}'.format)

    # Matplotlib and seaborn styling
    plt.style.use('default')
    sns.set_palette('husl')

    # Set figure size defaults
    plt.rcParams['figure.figsize'] = [12, 8]
    plt.rcParams['figure.dpi'] = 100


def load_game_sales_data(filepath: str = 'vgsales.csv') -> pd.DataFrame:
    """
    Load the video game sales dataset with error handling.

    Args:
        filepath: Path to the CSV file

    Returns:
        DataFrame containing the video game sales data

    Raises:
        FileNotFoundError: If the CSV file doesn't exist
        pd.errors.EmptyDataError: If the CSV file is empty
    """
    try:
        df = pd.read_csv(filepath)
        print(f'✅ Dataset loaded successfully from {filepath}')
        print(f'📊 Shape: {df.shape}')
        print(f'📋 Columns: {list(df.columns)}')
        return df
    except FileNotFoundError:
        print(f"❌ Error: File '{filepath}' not found")
        raise
    except pd.errors.EmptyDataError:
        print(f"❌ Error: File '{filepath}' is empty")
        raise
