import pandas as pd
import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns
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

# Parameters for days before and after
days_before =0
days_after = 0

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

# Include days before and after each adjusted LSAP date based on parameters
all_lsap_related_dates = adjusted_lsap_dates.tolist()
for date in adjusted_lsap_dates:
    if days_before != 0:
        if date.weekday() == 0 and days_before == 1:  # If the date is Monday and days_before is 1
            previous_friday = date - pd.Timedelta(days=3)  # Go back to Friday
            if previous_friday.weekday() == 4:  # Check if the previous day is actually a Friday
                all_lsap_related_dates.append(previous_friday)
        else:
            all_lsap_related_dates.append(date - pd.Timedelta(days=days_before))
    if days_after != 0:
        all_lsap_related_dates.append(date + pd.Timedelta(days=days_after))

# Ensure all relevant columns are numeric
cols_to_convert = ['WTI Close', 'VIX Close', 'MXWO Close', 'Expected CPI', 'ZN Close', 'DXY','CY']
data[cols_to_convert] = data[cols_to_convert].apply(pd.to_numeric, errors='coerce')

# Calculate returns
data['WTI_Log_Return'] = np.log(data['WTI Close'] / data['WTI Close'].shift(1))
data['VIX_Log_Return'] = np.log(data['VIX Close'] / data['VIX Close'].shift(1))
data['MXWO_Log_Return'] = np.log(data['MXWO Close'] / data['MXWO Close'].shift(1))
data['EI_Log_Change'] = np.log(data['Expected CPI'] / data['Expected CPI'].shift(1))
data['ZN_Log_Return'] = np.log(data['ZN Close'] / data['ZN Close'].shift(1))
data['DXY_Log_Return'] = np.log(data['DXY'] / data['DXY'].shift(1))


# Drop the first row with NaN values due to shift
data = data.dropna()

# Filter the data to include only the LSAP related dates
filtered_data = data[data['Date'].isin(all_lsap_related_dates)]

# Create LSAP announcement dummy variable
filtered_data['LSAP_Dummy'] = filtered_data['Date'].isin(adjusted_lsap_dates).astype(int)

# Ensure all necessary columns are present
required_columns = ['MXWO_Log_Return','EI_Log_Change', 'VIX_Log_Return', 'LSAP_Dummy', 'WTI_Log_Return','ZN_Log_Return','DXY_Log_Return']
if not all(col in filtered_data.columns for col in required_columns):
    raise ValueError("Not all required columns are present in the filtered data")

# Define the independent variables and the dependent variable
X = filtered_data[['DXY_Log_Return','EI_Log_Change','CY','COT','MXWO_Log_Return', 'VIX_Log_Return','ZN_Log_Return',]]
y = filtered_data['WTI_Log_Return']

# Add a constant to the independent variables
X = sm.add_constant(X)

# Run the regression
model = sm.OLS(y, X).fit()

# Print the regression results
print(model.summary())

# Pair plot with trendlines
variables = ['WTI_Log_Return', 'EI_Log_Change', 'DXY_Log_Return','CY']
plt.figure(figsize=(12, 8))
for i, var in enumerate(variables):
    plt.subplot(2, 2, i + 1)
    sns.regplot(x=var, y='WTI_Log_Return', data=filtered_data, scatter_kws={'alpha':0.5}, line_kws={'color':'red'})
    plt.title(f'{var} vs WTI Log Return')
    plt.xlabel(var)
    plt.ylabel('WTI Log Return')
plt.tight_layout()
plt.suptitle('Pair Plot: WTI Log Returns vs Economic Variables by LSAP Event', y=1.02)
plt.show()