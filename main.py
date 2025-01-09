import streamlit as st
from csv import excel
from large_scale_data.pandas_utils import convert_excel_to_csv



st.title("Large Scale Data Analyzer")

uploaded_file = st.file_uploader("Upload your data (excel)", type=excel)
st.write("Make sure your data is well structured, with titles for each column.")

sheet_name = st.text_input("If you wish to work only with a specific sheet in your data specify it here (case sensitive)")

if uploaded_file:
    try:
        if sheet_name:
            data= convert_excel_to_csv(uploaded_file, sheet_name=sheet_name)
        else:
            data = convert_excel_to_csv(uploaded_file, sheet_name=None)

        if isinstance(data, list):
            selected_sheet = st.selectbox("Choose a sheet to work on", data)
        else:
            if data:
                st.write(f"Generated CSV file: {data}")
            else:
                st.write("Error: No data was returned from the conversion.")
    except Exception as e:
        st.error(f"Error converting Excel to CSV: {e}")



