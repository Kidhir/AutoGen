import streamlit as st
import subprocess
import os

st.set_page_config(page_title="Multi-Agent EDA", layout="wide")
st.title("📊 Multi-Agent EDA System")
st.markdown("Upload a CSV file to perform exploratory data analysis using AI agents.")

uploaded_file = st.file_uploader("📁 Upload your CSV file", type="csv")

if uploaded_file:
    # Save uploaded CSV
    os.makedirs("data", exist_ok=True)
    data_path = os.path.join("data", "sample_dataset.csv")
    with open(data_path, "wb") as f:
        f.write(uploaded_file.read())
    st.success("✅ File uploaded successfully!")

    if st.button("🚀 Run EDA"):
        st.info("Running agents... this may take a minute.")
        with st.spinner("Agents are analyzing your dataset..."):
            try:
                result = subprocess.run(
                    ["python3", "eda_orchestrator.py"],
                    capture_output=True,
                    text=True,
                    check=True
                )
                st.success("✅ Analysis completed!")
                st.text("STDOUT:\n" + result.stdout)
                if result.stderr:
                    st.text("STDERR:\n" + result.stderr)
            except subprocess.CalledProcessError as e:
                st.error(f"❌ Failed to run EDA:\n{e}")
                st.text(e.stderr)
                st.stop()

        # Show the Markdown Report
        report_path = "outputs/eda_report.md"
        if os.path.exists(report_path):
            st.subheader("📄 EDA Report")
            with open(report_path, "r") as f:
                report = f.read()
                st.markdown(report, unsafe_allow_html=True)
        else:
            st.warning("⚠️ Report not found at outputs/eda_report.md")

        # Show the Pairplot
        plot_path = "outputs/pairplot.png"
        if os.path.exists(plot_path):
            st.subheader("📷 Pairplot Visualization")
            st.image(plot_path)
        else:
            st.warning("⚠️ Visualization not found at outputs/pairplot.png")
