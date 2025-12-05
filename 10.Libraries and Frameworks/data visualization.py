# Data Visualization in Python: Detailed Examples using matplotlib, seaborn, and plotly

# 1. Matplotlib - The foundation of Python data visualization

import matplotlib.pyplot as plt
import numpy as np

# Generate sample data
x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.figure(figsize=(8, 4))
plt.plot(x, y, label='sin(x)', color='blue', linestyle='--')
plt.title('Matplotlib Line Plot Example')
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# 2. Seaborn - Statistical data visualization built on matplotlib

import seaborn as sns
import pandas as pd

# Example DataFrame
df = pd.DataFrame({
    'Category': ['A', 'B', 'C', 'D'],
    'Values': [23, 45, 56, 78],
    'Labels': ['Alpha', 'Beta', 'Gamma', 'Delta']
})

# Bar plot with Seaborn
plt.figure(figsize=(6, 4))
sns.barplot(data=df, x='Category', y='Values', palette='pastel')
plt.title('Seaborn Bar Plot Example')
plt.xlabel('Category')
plt.ylabel('Values')
plt.tight_layout()
plt.show()

# Pairplot using seaborn with a numeric dataset
iris = sns.load_dataset('iris')
sns.pairplot(iris, hue='species', height=2)
plt.suptitle('Seaborn Pairplot Example (Iris Dataset)', y=1.02)
plt.show()

# 3. Plotly - Interactive visualizations

import plotly.express as px

# Scatter plot with Plotly
fig = px.scatter(iris, x='sepal_width', y='sepal_length',
                 color='species',
                 title='Plotly Interactive Scatter Plot (Iris Dataset)')
fig.show()

# Bar plot with Plotly
fig2 = px.bar(df, x='Labels', y='Values', color='Category',
              title='Plotly Interactive Bar Chart')
fig2.show()

