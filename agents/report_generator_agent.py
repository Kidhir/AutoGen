import os

def generate_report(summary):
    os.makedirs("outputs", exist_ok=True)
    with open("outputs/eda_report.md", "w") as f:
        f.write("# 📊 EDA Summary Report\n\n")
        f.write("The following table summarizes the dataset statistics:\n\n")
        f.write(summary.to_markdown())
