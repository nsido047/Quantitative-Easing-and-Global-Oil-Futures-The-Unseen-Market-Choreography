import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Load the Excel file
file_path = r"C:\Users\nsido\Desktop\Graduate\3. Masters - Summer 2024 (Reasearch Project)\Data\Other\CFTC_ICE_COT_Report.xlsx"
sheet_name = "COT_WTI"

# Read the data from the specified sheet
df = pd.read_excel(file_path, sheet_name=sheet_name)

# Ensure the Report_Date_as_YYYY_MM_DD column is in datetime format
df['Report_Date_as_YYYY_MM_DD'] = pd.to_datetime(df['Report_Date_as_YYYY_MM_DD'])

# Sort the data by date
df = df.sort_values(by='Report_Date_as_YYYY_MM_DD')

# Define the LSAP announcement dates and types (1 for easing, -1 for tightening)
lsap_data = {
    "11/25/2008": 1, "12/1/2008": 1, "12/16/2008": 1, "3/18/2009": 1,
    "8/12/2009": -1, "9/23/2009": -1, "11/4/2009": -1, "8/10/2010": 1,
    "11/3/2010": 1, "9/21/2011": 1, "9/13/2012": 1, "12/12/2012": 1,
    "12/18/2013": -1, "3/15/2020": 1, "3/23/2020": 1, "6/10/2020": 1,
    "11/3/2021": -1, "12/15/2021": -1, "1/26/2022": -1, "5/1/2024": -1
}

# Convert the LSAP dates to datetime
lsap_dates = pd.to_datetime(list(lsap_data.keys()))
lsap_types = list(lsap_data.values())

# Define the window size (in weeks) around each LSAP date
window_size = 4

# Plot each LSAP date and the open interest data around it
for lsap_date, lsap_type in zip(lsap_dates, lsap_types):
    start_date = lsap_date - pd.Timedelta(weeks=window_size)
    end_date = lsap_date + pd.Timedelta(weeks=window_size)
    
    # Filter the data to include only the dates within the window
    mask = (df['Report_Date_as_YYYY_MM_DD'] >= start_date) & (df['Report_Date_as_YYYY_MM_DD'] <= end_date)
    window_df = df[mask]
    
    plt.figure(figsize=(14, 8))
    plt.plot(window_df['Report_Date_as_YYYY_MM_DD'], window_df['Comm_Positions_Long_All'], label='Non-Commercial Long Positions')
    plt.plot(window_df['Report_Date_as_YYYY_MM_DD'], window_df['Comm_Positions_Short_All'], label='Non-Commercial Short Positions')
    
    # Mark the LSAP date
    color = 'green' if lsap_type == 1 else 'red'
    linestyle = '--' if lsap_type == 1 else '-.'
    plt.axvline(x=lsap_date, color=color, linestyle=linestyle, linewidth=2, label='Easing' if lsap_type == 1 else 'Tightening')
    
    # Add titles and labels
    plt.title(f'Non-Commercial Long and Short Positions for WTI Futures around LSAP Announcement on {lsap_date.date()}')
    plt.xlabel('Date')
    plt.ylabel('Open Interest')
    plt.legend()
    plt.grid(True)
    
    # Display the plot
    plt.show()
    
#%%
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rcParams

# Load the Excel file
file_path = r"C:\Users\nsido\Desktop\Graduate\3. Masters - Summer 2024 (Reasearch Project)\Data\Other\CFTC_ICE_COT_Report.xlsx"
sheet_name = "COT_WTI"

# Read the data from the specified sheet
df = pd.read_excel(file_path, sheet_name=sheet_name)

# Ensure the Report_Date_as_YYYY_MM_DD column is in datetime format
df['Report_Date_as_YYYY_MM_DD'] = pd.to_datetime(df['Report_Date_as_YYYY_MM_DD'])

# Sort the data by date
df = df.sort_values(by='Report_Date_as_YYYY_MM_DD')

# Define the LSAP announcement dates and types (1 for easing, -1 for tightening)
lsap_data = {
    "11/25/2008": 1, "12/1/2008": 1, "12/16/2008": 1, "3/18/2009": 1,
    "8/12/2009": -1, "9/23/2009": -1, "11/4/2009": -1, "8/10/2010": 1,
    "11/3/2010": 1, "9/21/2011": 1, "9/13/2012": 1, "12/12/2012": 1,
    "12/18/2013": -1, "3/15/2020": 1, "3/23/2020": 1, "6/10/2020": 1,
    "11/3/2021": -1, "12/15/2021": -1, "1/26/2022": -1, "5/1/2024": -1
}

# Convert the LSAP dates to datetime
lsap_dates = pd.to_datetime(list(lsap_data.keys()))
lsap_types = list(lsap_data.values())

# Initialize lists to store the changes
easing_changes = []
tightening_changes = []

# Calculate the changes around each LSAP date
for lsap_date, lsap_type in zip(lsap_dates, lsap_types):
    start_date = lsap_date - pd.Timedelta(weeks=1)
    end_date = lsap_date + pd.Timedelta(weeks=1)
    
    # Filter the data to include only the dates within the window
    mask = (df['Report_Date_as_YYYY_MM_DD'] >= start_date) & (df['Report_Date_as_YYYY_MM_DD'] <= end_date)
    window_df = df[mask]
    
    # Ensure there are enough data points in the window
    if len(window_df) > 1:
        # Calculate the change in long and short positions
        long_change = window_df['Comm_Positions_Long_All'].diff().iloc[-1]
        short_change = window_df['Comm_Positions_Short_All'].diff().iloc[-1]
        
        # Store the changes in the appropriate list
        if lsap_type == 1:
            easing_changes.append(long_change - short_change)
        else:
            tightening_changes.append(long_change - short_change)

# Create a DataFrame for the box plot
boxplot_data = pd.DataFrame({
    'Easing': easing_changes,
    'Tightening': tightening_changes
})

# Set font to Times New Roman
rcParams['font.family'] = 'serif'
rcParams['font.serif'] = 'Times New Roman'

# Increase DPI for high-quality print (300 DPI)
plt.figure(figsize=(10, 6), dpi=300)

# Plot the box plots
boxplot_data.plot(kind='box')
plt.ylabel('Change in Open Interest')
plt.grid(False)  # Disable grid lines

# Save the plot as a PDF file to the desktop
desktop_path = r"C:\Users\nsido\Desktop\Distribution of Commercial Open Interest Changes.pdf"
plt.savefig(desktop_path)

# Display the plot
plt.show()
#%%
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rcParams

# Load the Excel file
file_path = r"C:\Users\nsido\Desktop\Graduate\3. Masters - Summer 2024 (Reasearch Project)\Data\Other\CFTC_ICE_COT_Report.xlsx"
sheet_name = "COT_WTI"

# Read the data from the specified sheet
df = pd.read_excel(file_path, sheet_name=sheet_name)

# Ensure the Report_Date_as_YYYY_MM_DD column is in datetime format
df['Report_Date_as_YYYY_MM_DD'] = pd.to_datetime(df['Report_Date_as_YYYY_MM_DD'])

# Sort the data by date
df = df.sort_values(by='Report_Date_as_YYYY_MM_DD')

# Define the LSAP announcement dates and types (1 for easing, -1 for tightening)
lsap_data = {
    "11/25/2008": 1, "12/1/2008": 1, "12/16/2008": 1, "3/18/2009": 1,
    "8/12/2009": -1, "9/23/2009": -1, "11/4/2009": -1, "8/10/2010": 1,
    "11/3/2010": 1, "9/21/2011": 1, "9/13/2012": 1, "12/12/2012": 1,
    "12/18/2013": -1, "3/15/2020": 1, "3/23/2020": 1, "6/10/2020": 1,
    "11/3/2021": -1, "12/15/2021": -1, "1/26/2022": -1, "5/1/2024": -1
}

# Convert the LSAP dates to datetime
lsap_dates = pd.to_datetime(list(lsap_data.keys()))
lsap_types = list(lsap_data.values())

# Initialize lists to store the changes
easing_changes = []
tightening_changes = []

# Calculate the changes around each LSAP date
for lsap_date, lsap_type in zip(lsap_dates, lsap_types):
    start_date = lsap_date - pd.Timedelta(weeks=1)
    end_date = lsap_date + pd.Timedelta(weeks=1)
    
    # Filter the data to include only the dates within the window
    mask = (df['Report_Date_as_YYYY_MM_DD'] >= start_date) & (df['Report_Date_as_YYYY_MM_DD'] <= end_date)
    window_df = df[mask]
    
    # Ensure there are enough data points in the window
    if len(window_df) > 1:
        # Calculate the change in long and short positions
        long_change = window_df['NonComm_Positions_Long_All'].diff().iloc[-1]
        short_change = window_df['NonComm_Positions_Short_All'].diff().iloc[-1]
        
        # Store the changes in the appropriate list
        if lsap_type == 1:
            easing_changes.append(long_change - short_change)
        else:
            tightening_changes.append(long_change - short_change)

# Create a DataFrame for the box plot
boxplot_data = pd.DataFrame({
    'Easing': easing_changes,
    'Tightening': tightening_changes
})

# Set font to Times New Roman
rcParams['font.family'] = 'serif'
rcParams['font.serif'] = 'Times New Roman'

# Increase DPI for high-quality print (300 DPI)
plt.figure(figsize=(10, 6), dpi=300)

# Plot the box plots
boxplot_data.plot(kind='box')
plt.ylabel('Change in Open Interest')
plt.grid(False)  # Disable grid lines

# Save the plot as a PDF file to the desktop
desktop_path = r"C:\Users\nsido\Desktop\Distribution of Non-Commercial Open Interest Changes.pdf"
plt.savefig(desktop_path)

# Display the plot
plt.show()
