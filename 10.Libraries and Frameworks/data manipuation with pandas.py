import pandas as pd

# 1. Creating a DataFrame from a dictionary
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'Salary': [70000, 80000, 90000]
}
df = pd.DataFrame(data)
print("Step 1: Created DataFrame from dictionary:")
print(df)
print("-" * 50)

# 2. Reading and writing CSV files
# Reading a CSV file into a DataFrame
# Uncomment and set your filename to use:
# df_from_csv = pd.read_csv('your_filename.csv')
# print("Step 2a: Loaded DataFrame from CSV:\n", df_from_csv)

# Writing a DataFrame to a CSV file (no index column)
# Uncomment to save your DataFrame:
# df.to_csv('output.csv', index=False)
# print("Step 2b: DataFrame written to output.csv")

print("Step 2: (CSV read/write skipped in this demo)")
print("-" * 50)

# 3. Inspecting DataFrame structure & info
print("Step 3: DataFrame info:")
print(df.info())
print("DataFrame summary statistics:")
print(df.describe())
print("-" * 50)

# 4. Selecting columns and rows

# a) Selecting a single column (as Series)
ages_series = df['Age']
print("Step 4a: 'Age' column (Series):")
print(ages_series)

# b) Selecting multiple columns (as DataFrame)
subset_df = df[['Name', 'Salary']]
print("Step 4b: 'Name' and 'Salary' columns (DataFrame):")
print(subset_df)

# c) Selecting rows by position (iloc)
first_two_rows = df.iloc[:2]
print("Step 4c: First two rows using iloc:")
print(first_two_rows)

# d) Selecting rows by condition (boolean indexing)
over_30 = df[df['Age'] > 30]
print("Step 4d: Rows where Age > 30:")
print(over_30)
print("-" * 50)

# 5. Filtering rows by column condition
high_salary = df[df['Salary'] > 75000]
print("Step 5: Rows with Salary > 75000:")
print(high_salary)
print("-" * 50)

# 6. Adding new columns

# a) Add a new column by list
df['Seniority'] = ['Junior', 'Mid', 'Senior']
print("Step 6a: Added 'Seniority' column:")
print(df)

# b) Add calculated columns inline (e.g., salary in thousands)
df['Salary_k'] = df['Salary'] / 1000
print("Step 6b: Added calculated column 'Salary_k':")
print(df)
print("-" * 50)

# 7. Modifying values with apply/lambda
df['Age_plus_1'] = df['Age'].apply(lambda x: x + 1)
print("Step 7: Added 'Age_plus_1' by applying a function to 'Age':")
print(df)
print("-" * 50)

# 8. Removing (dropping) columns and rows
dropped_df = df.drop(columns=['Salary_k', 'Age_plus_1'])
print("Step 8: DataFrame after dropping 'Salary_k' and 'Age_plus_1':")
print(dropped_df)
print("-" * 50)

# 9. Sorting the DataFrame
sorted_df = df.sort_values(by='Salary', ascending=False)
print("Step 9: DataFrame sorted by 'Salary' descending:")
print(sorted_df)
print("-" * 50)

# 10. Grouping and aggregation
average_salary = df.groupby('Seniority')['Salary'].mean()
print("Step 10: Average Salary by Seniority (GroupBy):")
print(average_salary)
print("-" * 50)

# 11. Handling missing data
# Introduce missing data for example
df.loc[2, 'Salary'] = None
print("Step 11a: DataFrame with a missing value in 'Salary':")
print(df)

# Fill missing values
df_filled = df.fillna({'Salary': df['Salary'].mean()})
print("Step 11b: DataFrame after filling missing 'Salary' value with mean:")
print(df_filled)
print("-" * 50)

# 12. Resetting index
reset_df = df.reset_index(drop=True)
print("Step 12: DataFrame after resetting index:")
print(reset_df)
print("-" * 50)