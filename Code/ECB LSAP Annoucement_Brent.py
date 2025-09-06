import pandas as pd
import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm

# Load the data from the Excel file
file_path = "C:\\Users\\nsido\\Desktop\\Graduate\\3. Masters - Summer 2024 (Reasearch Project)\\Data\\Bloomberg\\Data.xlsx"
sheet_name = "ECB_MASTER"
data = pd.read_excel(file_path, sheet_name=sheet_name)

# Convert the Date column to datetime format
data['Date'] = pd.to_datetime(data['Date'])

# LSAP announcement dates
lsap_dates = [
    '2010-05-10',
    '2011-08-07',
    '2011-10-06',
    '2012-09-06',
    '2014-10-02',
    '2015-01-22',
    '2016-04-21',
    '2017-10-26',
    '2018-12-13',
    '2020-03-18',
    '2020-06-04',
    '2020-12-10',
    '2021-03-11',
    '2021-09-08',
    '2021-12-16',
    '2023-12-14'
]

lsap_dates = pd.to_datetime(lsap_dates)

# Parameters for days before and after
days_before = 0
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

# Remove duplicates from all_lsap_related_dates
all_lsap_related_dates = list(set(all_lsap_related_dates))

# Calculate returns
data['Brent_Log_Return'] = np.log(data['Brent Close'] / data['Brent Close'].shift(1))
data['VIX_Log_Return'] = np.log(data['VIX Close'] / data['VIX Close'].shift(1))
data['MXWO_Log_Return'] = np.log(data['MXWO Close'] / data['MXWO Close'].shift(1))
data['EUR/USD_Log_Return'] = np.log(data['EUR/USD'] / data['EUR/USD'].shift(1))

# Drop the first row with NaN values due to shift
data = data.dropna()

# Filter the data to include only the LSAP related dates
filtered_data = data[data['Date'].isin(all_lsap_related_dates)]

# Create LSAP announcement dummy variable
filtered_data['LSAP_Dummy'] = filtered_data['Date'].isin(adjusted_lsap_dates).astype(int)

# Ensure all necessary columns are present
required_columns = ['MXWO_Log_Return', 'VIX_Log_Return', 'LSAP_Dummy', 'Brent_Log_Return','EUR/USD_Log_Return']
if not all(col in filtered_data.columns for col in required_columns):
    raise ValueError("Not all required columns are present in the filtered data")

# Define the independent variables and the dependent variable
X = filtered_data[['EUR/USD_Log_Return','MXWO_Log_Return', 'VIX_Log_Return', 'LSAP_Dummy']]
y = filtered_data['Brent_Log_Return']

# Add a constant to the independent variables
X = sm.add_constant(X)

# Run the regression
model = sm.OLS(y, X).fit()

# Print the regression results
print(model.summary())

# Pair plot with trendlines
variables = ['Brent_Log_Return', 'MXWO_Log_Return', 'VIX_Log_Return', 'EUR/USD_Log_Return']
plt.figure(figsize=(12, 8))
for i, var in enumerate(variables):
    plt.subplot(2, 2, i + 1)
    sns.regplot(x=var, y='Brent_Log_Return', data=filtered_data, scatter_kws={'alpha':0.5}, line_kws={'color':'red'})
    plt.title(f'{var} vs Brent Log Return')
    plt.xlabel(var)
    plt.ylabel('Brent Log Return')
plt.tight_layout()
plt.suptitle('Pair Plot: Economic Variables vs WTI Log Return by LSAP Event', y=1.02)
plt.show()
