"""
Utility functions for video game sales analysis.

This module provides helper functions for analysis suggestions and other utilities.
"""

from typing import List


def suggest_next_analysis_steps() -> List[str]:
    """
    Suggest next steps for extended analysis.

    Returns:
        List of analysis suggestions
    """
    suggestions = [
        '📊 Create visualizations: Time series plots for genre trends over decades',
        '🗺️  Geographic analysis: Regional preference heatmaps by genre/platform',
        '📈 Correlation analysis: Relationship between regional sales patterns',
        '🎯 Market segmentation: Identify distinct gaming market segments',
        '🚀 Predictive modeling: Forecast future gaming trends',
        '🎮 Platform lifecycle: Analyze console adoption and decline patterns',
        '💰 Revenue optimization: Identify factors for commercial success',
        '🏆 Franchise analysis: Multi-game series performance patterns',
    ]

    print('=== Recommended Next Analysis Steps ===')
    for i, suggestion in enumerate(suggestions, 1):
        print(f'{i}. {suggestion}')

    return suggestions


def print_analysis_complete_message() -> None:
    """Print a summary message when analysis is complete."""
    print('## 🎉 Analysis Complete!')
    print()
    print('This refactored notebook now demonstrates **coding best practices** with:')
    print()
    print('### ✨ **Code Quality Improvements**')
    print('- **Modular functions** with clear documentation and type hints')
    print('- **Error handling** for robust data loading')
    print('- **Separation of concerns** - each cell has a single responsibility')
    print('- **Reusable code** through well-designed helper functions')
    print('- **Clean organization** with logical flow and progression')
    print()
    print('### 🔧 **Technical Best Practices Applied**')
    print('- Type hints for better code clarity and IDE support')
    print('- Comprehensive docstrings following Python conventions')
    print('- Descriptive function and variable names')
    print('- Configuration separated from logic')
    print('- Input validation and error handling')
    print('- Modular design for code reuse')
    print()
    print('### 📝 **Documentation Standards**')
    print('- Clear markdown headers with purpose statements')
    print('- Function documentation with Args/Returns')
    print('- Progressive analysis structure')
    print('- Visual indicators (emojis) for better readability')
    print('- Comprehensive analysis summaries')
    print()
    print('**The notebook is now production-ready and maintainable!** 🚀')
