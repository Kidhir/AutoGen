import pandas as pd
from agents.eda_agent import run_eda
from agents.report_generator_agent import generate_report
import os

# Load data
df = pd.read_csv("data/sample_dataset.csv")

# Run EDA
summary = run_eda(df)

# Generate markdown report
generate_report(summary)

print("✅ EDA Completed. Outputs saved to /outputs")
