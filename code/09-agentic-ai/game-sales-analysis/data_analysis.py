"""
Data analysis functions for video game sales research.

This module provides comprehensive analysis functions for exploring video game sales data,
including missing data analysis, distribution analysis, and market insights.
"""

import pandas as pd
from typing import Dict, List, Tuple, Union


def analyze_missing_data(df: pd.DataFrame) -> Dict[str, int]:
    """
    Analyze missing data in the DataFrame.

    Args:
        df: DataFrame to analyze

    Returns:
        Dictionary with column names and missing value counts
    """
    missing_values = df.isnull().sum()
    missing_dict = missing_values[missing_values > 0].to_dict()

    print('=== Missing Values Analysis ===')
    if missing_dict:
        for col, count in missing_dict.items():
            print(f'📊 {col}: {count:,} missing values ({count / len(df) * 100:.2f}%)')
    else:
        print('✅ No missing values found!')

    return missing_dict


def get_top_performers(df: pd.DataFrame, column: str, n: int = 10) -> pd.DataFrame:
    """
    Get top N performers by a specified column.

    Args:
        df: DataFrame to analyze
        column: Column to sort by
        n: Number of top performers to return

    Returns:
        DataFrame with top N performers
    """
    return df.nlargest(n, column)


def analyze_distribution(df: pd.DataFrame, column: str, top_n: int = 15) -> pd.Series:
    """
    Analyze the distribution of values in a column.

    Args:
        df: DataFrame to analyze
        column: Column to analyze
        top_n: Number of top values to show

    Returns:
        Series with value counts
    """
    distribution = df[column].value_counts().head(top_n)

    print(f'=== {column} Distribution (Top {top_n}) ===')
    print(distribution)
    print(f'\nTotal unique values: {df[column].nunique():,}')

    return distribution


def calculate_regional_breakdown(df: pd.DataFrame, game_names: Union[List[str], int]) -> pd.DataFrame:
    """
    Calculate regional sales breakdown for specific games.

    Args:
        df: DataFrame containing sales data
        game_names: List of game names to analyze or integer for top N games

    Returns:
        DataFrame with regional sales breakdown
    """
    regional_cols = ['Name', 'NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales', 'Global_Sales']

    if isinstance(game_names, int):
        # If integer passed, get top N games
        return df.head(game_names)[regional_cols]
    else:
        # If list of names passed, filter by those names
        filtered_df = df[df['Name'].isin(game_names)]
        return filtered_df[regional_cols]


def analyze_publishers(df: pd.DataFrame, top_n: int = 10) -> Tuple[pd.Series, pd.Series]:
    """
    Analyze publishers by number of games and total sales.

    Args:
        df: DataFrame to analyze
        top_n: Number of top publishers to show

    Returns:
        Tuple of (games_count, total_sales) Series
    """
    print(f'=== Top {top_n} Publishers by Number of Games ===')
    publisher_games = df['Publisher'].value_counts().head(top_n)
    print(publisher_games)

    print(f'\n=== Top {top_n} Publishers by Total Global Sales ===')
    publisher_sales = df.groupby('Publisher')['Global_Sales'].sum().sort_values(ascending=False).head(top_n)
    print(publisher_sales.round(2))

    return publisher_games, publisher_sales


def analyze_year_trends(df: pd.DataFrame) -> Dict[str, any]:
    """
    Analyze gaming trends by year.

    Args:
        df: DataFrame to analyze

    Returns:
        Dictionary with year analysis results
    """
    # Filter out missing years
    df_with_years = df.dropna(subset=['Year'])

    # Calculate basic year statistics
    year_stats = {
        'earliest_year': df_with_years['Year'].min(),
        'latest_year': df_with_years['Year'].max(),
        'median_year': df_with_years['Year'].median(),
        'games_per_year': df_with_years.groupby('Year').size().describe(),
    }

    print('=== Gaming Industry Timeline ===')
    print(f'📅 Dataset covers: {year_stats["earliest_year"]:.0f} - {year_stats["latest_year"]:.0f}')
    print(f'📊 Median release year: {year_stats["median_year"]:.0f}')
    games_by_year = df_with_years.groupby("Year").size()
    peak_year = games_by_year.idxmax()
    peak_count = games_by_year.max()
    print(f'🎮 Peak gaming year: {peak_year:.0f} ({peak_count} games)')

    return year_stats


def get_regional_market_share(df: pd.DataFrame) -> Dict[str, float]:
    """
    Calculate global market share by region.

    Args:
        df: DataFrame with regional sales data

    Returns:
        Dictionary with regional market shares
    """
    total_na = df['NA_Sales'].sum()
    total_eu = df['EU_Sales'].sum()
    total_jp = df['JP_Sales'].sum()
    total_other = df['Other_Sales'].sum()
    total_global = total_na + total_eu + total_jp + total_other

    market_share = {
        'North America': (total_na / total_global) * 100,
        'Europe': (total_eu / total_global) * 100,
        'Japan': (total_jp / total_global) * 100,
        'Other': (total_other / total_global) * 100,
    }

    print('=== Global Market Share by Region ===')
    for region, share in market_share.items():
        print(f'🌍 {region}: {share:.1f}%')

    return market_share


def generate_summary_statistics(df: pd.DataFrame) -> Dict[str, any]:
    """
    Generate comprehensive summary statistics for the dataset.

    Args:
        df: DataFrame to analyze

    Returns:
        Dictionary with summary statistics
    """
    summary = {
        'total_games': len(df),
        'total_sales': df['Global_Sales'].sum(),
        'average_sales': df['Global_Sales'].mean(),
        'unique_platforms': df['Platform'].nunique(),
        'unique_genres': df['Genre'].nunique(),
        'unique_publishers': df['Publisher'].nunique(),
        'year_range': (df['Year'].min(), df['Year'].max()),
        'top_selling_game': df.loc[df['Global_Sales'].idxmax(), 'Name'],
        'nintendo_dominance': (df['Publisher'] == 'Nintendo').sum() / len(df) * 100,
    }

    print('=== Dataset Summary Statistics ===')
    print(f'🎮 Total games analyzed: {summary["total_games"]:,}')
    print(f'💰 Total global sales: {summary["total_sales"]:.2f}M copies')
    print(f'📊 Average sales per game: {summary["average_sales"]:.2f}M copies')
    print(f'🕹️  Unique platforms: {summary["unique_platforms"]}')
    print(f'🎯 Unique genres: {summary["unique_genres"]}')
    print(f'🏢 Unique publishers: {summary["unique_publishers"]}')
    print(f'👑 Top selling game: {summary["top_selling_game"]}')
    print(f'🎯 Nintendo market presence: {summary["nintendo_dominance"]:.1f}% of all games')

    return summary
