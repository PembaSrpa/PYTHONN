# ydata-profiling
# Example: Using ydata-profiling to quickly analyze a DataFrame

# 1. Install ydata-profiling if you haven't:
#    pip install ydata-profiling

import pandas as pd
from ydata_profiling import ProfileReport

# Sample DataFrame
data = {
    "name": ["Alice", "Bob", "Charlie", "David"],
    "age": [23, 35, 31, 29],
    "salary": [70000, 80000, 65000, 90000]
}
df = pd.DataFrame(data)

# Create a ProfileReport using ydata-profiling
profile = ProfileReport(df, title="ydata-profiling Report", explorative=True)

# Save the report to an HTML file
profile.to_file("ydata_report.html")

print("ydata-profiling report saved as ydata_report.html")

# Explanation:
#
# The above code demonstrates how to use the `ydata-profiling` library (formerly `pandas-profiling`), an AI-powered tool for automatic exploratory data
# analysis (EDA) of pandas DataFrames. When you run this script, it creates a detailed HTML report summarizing the dataset's characteristics—
# such as column types, missing values, unique values, statistics for numericals, correlations, and sample data. This is very helpful for
# quickly understanding your data, especially in the early stages of data science and machine learning projects.
#
# Key steps:
# 1. You load your data into a pandas DataFrame.
# 2. You use `ProfileReport` (from ydata-profiling) to generate a report summarizing the DataFrame.
# 3. You save the report as an HTML file, which you can view in your browser.
#
# Tools like ydata-profiling streamline routine analysis, speed up data exploration, and highlight issues (such as missing values or duplicates) that may require attention.

# Note:
# As of 2024, `ydata-profiling` is the actively maintained version of the formerly named `pandas-profiling` library. It may require Python 3.7-3.12.
# Always check current compatibility with your Python version in their docs.
