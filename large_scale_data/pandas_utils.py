import pandas as pd

def convert_excel_to_csv(uploaded_file, sheet_name = None):
    excel_data = pd.read_excel(uploaded_file, sheet_name=sheet_name)

    try:
        if isinstance(excel_data, dict):
            csv_files = []
            for name, df in excel_data.items():
                csv_file = f"{name}_output.csv"
                df.to_csv(csv_file, index=False)
                csv_files.append(csv_file)
            return csv_files
        else:
            csv_file = "output.csv"
            excel_data.to_csv(csv_file, index=False)
            return csv_file

    except exception as e:
        print(f"Error converting Excel to CSV: {e}")
        return None

