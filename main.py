import pandas as pd
import streamlit as st
from large_scale_data.pandas_utils import convert_excel_to_csv, plot_data

st.title("Large Scale Data Analyzer")

sheet_name = st.text_input("If you wish to work only with a specific sheet in your data specify it here (case sensitive)")

uploaded_file = st.file_uploader("Upload your data (excel files only, .xlsx or .xls)", type=["xlsx", "xls"])
st.markdown("""
Make sure your data is well structured, with titles for each column.
  
Make sure you understand your data. Your graphs will not make sense if you choose the wrong plot type.  
For example - in the diamond data set, plotting price against carat using a line plot won't yield a sensible graph, you will need to use a different type of graph.
""")

data = None
df = None
x_axis = None
y_axis = None

if uploaded_file:
    try:
        if sheet_name:
            data= convert_excel_to_csv(uploaded_file, sheet_name=sheet_name)
        else:
            data = convert_excel_to_csv(uploaded_file, sheet_name=None)

    except Exception as e:
        st.error(f"Error converting Excel to CSV: {e}")

if isinstance(data, list):
    selected_sheet = st.selectbox("Choose a sheet to work on", data)
    if selected_sheet:
        for sheet in data:
            if sheet == selected_sheet:
                df = pd.read_csv(sheet)

else:
    if data:
        st.write(f"Generated CSV file: {data}")
        df = pd.read_csv(data)
    else:
        st.write("Error: No data was returned from the conversion.")

with st.container():
    if df is not None:
        x_axis = st.selectbox(
            "What column is your x-axis?",
            df.columns,
            help="column"
        )
        if x_axis:
            y_axes = st.multiselect(
            "What column are your y-axes?",
            df.columns,
            help="column"
        )
    if x_axis and y_axes:
        columns_per_row = 2

        for i, y_axis in enumerate(y_axes):
            if i % columns_per_row == 0:
                cols = st.columns(columns_per_row)

            fig = plot_data(df, x_axis, y_axis)

            col_index = i % columns_per_row
            with cols[col_index]:
                st.pyplot(fig)

