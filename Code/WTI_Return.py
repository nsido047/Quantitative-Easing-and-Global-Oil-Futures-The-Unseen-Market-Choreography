import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm

# Load the data from the Excel file
file_path = "C:\\Users\\nsido\\Desktop\\Graduate\\3. Masters - Summer 2024 (Reasearch Project)\\Data\\Bloomberg\\Data.xlsx"
sheet_name = "FED_MASTER"
data = pd.read_excel(file_path, sheet_name=sheet_name)

# Convert the Date column to datetime format
data['Date'] = pd.to_datetime(data['Date'])

# LSAP announcement dates
lsap_dates = [
    '2008-11-25', '2008-12-01', '2008-12-16', '2009-03-18',
    '2009-08-12', '2009-09-23', '2009-11-04', '2010-08-10', '2010-11-03',
    '2011-09-21', '2012-09-13', '2012-12-12', '2013-12-18', '2020-03-15',
    '2020-03-23', '2020-06-10', '2021-11-03', '2021-12-15',
    '2022-01-26', '2024-05-01'
]
lsap_dates = pd.to_datetime(lsap_dates)

# Adjust LSAP dates that fall on weekends to the following Monday
adjusted_lsap_dates = []
for date in lsap_dates:
    if date.weekday() >= 5:  # If the date is Saturday (5) or Sunday (6)
        # Find the next Monday
        next_monday = date + pd.Timedelta(days=(7 - date.weekday()))
        adjusted_lsap_dates.append(next_monday)
    else:
        adjusted_lsap_dates.append(date)
adjusted_lsap_dates = pd.to_datetime(adjusted_lsap_dates)

# Calculate log returns
data['WTI_Log_Return'] = np.log(data['WTI Close'] / data['WTI Close'].shift(1))
data['VIX_Log_Return'] = np.log(data['VIX Close'] / data['VIX Close'].shift(1))
data['MXWO_Log_Return'] = np.log(data['MXWO Close'] / data['MXWO Close'].shift(1))
data['ZN_Log_Return'] = np.log(data['ZN Close'] / data['ZN Close'].shift(1))

# Drop the first row with NaN values due to shift
data = data.dropna()

# Plot log returns around each LSAP announcement date
for date in adjusted_lsap_dates:
    # Define the window around the LSAP date
    window_start = date - pd.Timedelta(days=2)
    window_end = date + pd.Timedelta(days=2)
    
    # Filter data for the window
    window_data = data[(data['Date'] >= window_start) & (data['Date'] <= window_end)]
    
    # Plot
    plt.figure(figsize=(10, 5))
    plt.plot(window_data['Date'], window_data['WTI_Log_Return'], marker='o', linestyle='-')
    plt.axvline(x=date, color='r', linestyle='--', label='LSAP Announcement')
    plt.title(f'WTI Log Returns around LSAP Announcement on {date.strftime("%Y-%m-%d")}')
    plt.xlabel('Date')
    plt.ylabel('WTI Log Return')
    plt.xticks(window_data['Date'], window_data['Date'].dt.strftime('%m-%d'), rotation=45)
    plt.legend()
    plt.grid(True)
    plt.show()

