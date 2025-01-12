import pandas as pd
import streamlit as st
import openpyxl
import os
import matplotlib.pyplot as plt
from matplotlib.lines import lineStyles


@st.cache_data
def convert_excel_to_csv(uploaded_file, sheet_name = None, output_dir=r'C:\Users\idosc\Documents\GitHub\output'):
    excel_data = pd.read_excel(uploaded_file, sheet_name=sheet_name)

    try:
        if isinstance(excel_data, dict):
            csv_files = []
            for name, df in excel_data.items():
                csv_file = os.path.join(output_dir, f"{name}_output.csv")
                df.to_csv(csv_file, index=False)
                csv_files.append(csv_file)
            return csv_files
        else:
            csv_file = os.path.join(output_dir, "output.csv")
            excel_data.to_csv(csv_file, index=False)
            return csv_file

    except Exception as e:
        print(f"Error converting Excel to CSV: {e}")
        return None

def plot_data(df, x_axis, y_axis):
    fig, ax = plt.subplots(figsize=(10, 6))
    if pd.api.types.is_numeric_dtype(df[y_axis]):
        ax.plot(df[x_axis], df[y_axis], marker = 'o', linestyle = '-')
        ax.set_title(f"line plot for {y_axis}")
        ax.set_xlabel(x_axis)
        ax.set_ylabel(y_axis)
    else:
        categories = df[y_axis].value_counts()
        ax.bar(categories.index, categories.values, label=y_axis)
        ax.set_title(f"Bar Chart for {y_axis}")
        ax.set_xlabel(y_axis)
        ax.set_ylabel("Count")

    ax.legend()
    plt.tight_layout()
    return fig