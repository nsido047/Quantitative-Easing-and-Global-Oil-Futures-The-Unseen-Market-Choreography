import pandas as pd
import numpy as np

# Path to the Excel file and sheet name
file_path = r"C:\Users\nsido\Desktop\Graduate\3. Masters - Summer 2024 (Reasearch Project)\Data\Other\CFTC_ICE_COT_Report.xlsx"
sheet_name = "Legacy_COT_Brent"
output_file_path = r"C:\Users\nsido\Desktop\Graduate\3. Masters - Summer 2024 (Reasearch Project)\Data\Other\CFTC_ICE_COT_Report_Results.xlsx"

# Load the dataset from the Excel file
df = pd.read_excel(file_path, sheet_name=sheet_name)

# Convert 'Date' column to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Function to find the log change between the current and previous date
def get_log_weekly_change(df):
    log_changes = []
    for i in range(1, len(df)):
        current_row = df.iloc[i]
        previous_row = df.iloc[i-1]
        log_change = np.log(current_row['Open Interest'] / previous_row['Open Interest'])
        log_changes.append({
            'Current Date': current_row['Date'],
            'Previous Date': previous_row['Date'],
            'Log Change': log_change
        })
    return log_changes

# Calculate log changes for all dates
log_changes = get_log_weekly_change(df)

# Convert results to DataFrame
log_changes_df = pd.DataFrame(log_changes)

# Output the results to a new Excel file
with pd.ExcelWriter(output_file_path, engine='openpyxl') as writer:
    log_changes_df.to_excel(writer, index=False, sheet_name='Log Changes')

print(f"Results have been written to {output_file_path}")
