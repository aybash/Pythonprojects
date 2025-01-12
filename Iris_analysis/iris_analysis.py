import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# Load and Explore the Dataset
def load_and_explore_iris():
  
    try:
        # Load Iris dataset from sklearn
        iris = load_iris()
        data = pd.DataFrame(iris.data, columns=iris.feature_names)
        data['species'] = pd.Categorical.from_codes(iris.target, iris.target_names)

        print("Iris Dataset loaded successfully!")
        print("\n--- First 5 Rows ---")
        print(data.head())

        print("\n--- Data Info ---")
        print(data.info())

        print("\n--- Missing Values ---")
        print(data.isnull().sum())

        return data
    except Exception as e:
        print(f"An error occurred: {e}")

# Basic Data Analysis
def basic_analysis(data):
   
    print("\n--- Basic Statistics ---")
    print(data.describe())

    print("\n--- Group Means by Species ---")
    group_means = data.groupby("species").mean()
    print(group_means)

    print("\n--- Observations ---")
    print("The setosa species tends to have smaller petal lengths and widths compared to others.")

# Data Visualization
def create_iris_visualizations(data):
   
    # Line chart
    plt.figure(figsize=(10, 6))
    plt.plot(data.index, data['petal length (cm)'], label='Petal Length')
    plt.title("Trends in Petal Length Across Samples")
    plt.xlabel("Sample Index")
    plt.ylabel("Petal Length (cm)")
    plt.legend()
    plt.show()

    # Bar chart: Average petal length by species
    plt.figure(figsize=(8, 6))
    sns.barplot(x="species", y="petal length (cm)", data=data, palette="viridis")
    plt.title("Average Petal Length by Species")
    plt.xlabel("Species")
    plt.ylabel("Petal Length (cm)")
    plt.show()

    # Histogram: Sepal length distribution
    plt.figure(figsize=(8, 6))
    sns.histplot(data["sepal length (cm)"], kde=True, bins=15, color="skyblue")
    plt.title("Distribution of Sepal Length")
    plt.xlabel("Sepal Length (cm)")
    plt.ylabel("Frequency")
    plt.show()

    # Scatter plot: Sepal length vs. petal length by species
    plt.figure(figsize=(8, 6))
    sns.scatterplot(
        x="sepal length (cm)",
        y="petal length (cm)",
        hue="species",
        data=data,
        palette="deep"
    )
    plt.title("Sepal Length vs. Petal Length by Species")
    plt.xlabel("Sepal Length (cm)")
    plt.ylabel("Petal Length (cm)")
    plt.legend(title="Species")
    plt.show()

# Main Execution
if __name__ == "__main__":

    iris_data = load_and_explore_iris()

    if iris_data is not None:
        
        basic_analysis(iris_data)

        
        create_iris_visualizations(iris_data)
