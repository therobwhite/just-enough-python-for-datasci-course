"""
Video Game Sales Analysis Package

This package provides comprehensive tools for analyzing video game sales data.

Modules:
--------
- data_loader: Functions for loading and configuring data analysis environment
- data_analysis: Core analysis functions for sales data exploration
- utils: Utility functions for suggestions and reporting

Example Usage:
--------------
    from data_loader import load_game_sales_data, setup_display_options
    from data_analysis import analyze_missing_data, get_top_performers
    
    # Set up environment
    setup_display_options()
    
    # Load and analyze data
    df = load_game_sales_data()
    missing_info = analyze_missing_data(df)
    top_games = get_top_performers(df, 'Global_Sales', 10)
"""

__version__ = "1.0.0"
__author__ = "Video Game Sales Research Team"

# Import main functions for easy access
from .data_loader import setup_display_options, load_game_sales_data
from .data_analysis import (
    analyze_missing_data,
    get_top_performers,
    analyze_distribution,
    calculate_regional_breakdown,
    analyze_publishers,
    analyze_year_trends,
    get_regional_market_share,
    generate_summary_statistics,
)
from .utils import suggest_next_analysis_steps, print_analysis_complete_message

__all__ = [
    "setup_display_options",
    "load_game_sales_data",
    "analyze_missing_data",
    "get_top_performers",
    "analyze_distribution",
    "calculate_regional_breakdown",
    "analyze_publishers",
    "analyze_year_trends",
    "get_regional_market_share",
    "generate_summary_statistics",
    "suggest_next_analysis_steps",
    "print_analysis_complete_message",
]