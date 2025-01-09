import pandas as pd
import streamlit as st
import openpyxl
import os

@st.cache_data
def convert_excel_to_csv(uploaded_file, sheet_name = None, output_dir='./output/'):
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

