# eda_orchestrator.py

import pandas as pd
from agents.eda_agent import run_eda
from agents.report_generator_agent import generate_report
import os

# Load CSV
data_path = "data/sample_dataset.csv"
if not os.path.exists(data_path):
    raise FileNotFoundError("sample_dataset.csv not found in /data folder")

df = pd.read_csv(data_path)

# Run EDA
print("🔄 Cleaning data...")
summary = run_eda(df)

# Write report
print("📝 Writing report...")
generate_report(summary)

print("✅ Done: Report and plot written to /outputs")
