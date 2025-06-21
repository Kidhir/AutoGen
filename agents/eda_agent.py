import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

def run_eda(df: pd.DataFrame):
    os.makedirs("outputs", exist_ok=True)

    # Generate summary statistics
    summary = df.describe(include='all')

    # Generate a pairplot (only for numerical columns)
    numeric_df = df.select_dtypes(include=['number'])
    if not numeric_df.empty:
        plot = sns.pairplot(numeric_df)
        plot.fig.suptitle("Pairplot of Numeric Features", y=1.02)
        plt.tight_layout()
        plt.savefig("outputs/pairplot.png")
        plt.close()

    return summary
