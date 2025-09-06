import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# Set global font to Times New Roman
plt.rcParams["font.family"] = "Times New Roman"

# Load the data from the Excel file
file_path = 'C:\\Users\\nsido\\Desktop\\Graduate\\3. Masters - Summer 2024 (Reasearch Project)\\Analysis\\Figure Data_2024-07-19.xlsx'
sheet_name = 'Figure 3'
data = pd.read_excel(file_path, sheet_name=sheet_name)

# Parse dates and sort the data by date
data['Date'] = pd.to_datetime(data['Date'])
data.sort_values('Date', inplace=True)

# List of QE announcement dates
qe_dates = [
    '2008-11-25', '2008-12-01', '2008-12-16', '2009-03-18', '2009-08-12',
    '2009-09-23', '2009-11-04', '2010-08-10', '2010-11-03', '2011-09-21',
    '2012-09-13', '2012-12-12', '2013-12-18', '2020-03-15', '2020-03-23',
    '2020-06-10', '2021-11-03', '2021-12-15', '2022-01-26', '2024-05-01'
]
qe_dates = pd.to_datetime(qe_dates)

# Filter function to plot data within a specified date range
def plot_brent_eurusd(start_date, end_date):
    # Convert start_date and end_date to datetime format
    start_date = pd.to_datetime(start_date)
    end_date = pd.to_datetime(end_date)
    
    # Filter data within the specified date range
    filtered_data = data[(data['Date'] >= start_date) & (data['Date'] <= end_date)]

    # Find the closest dates in the data for each QE announcement date
    closest_dates = []
    for qe_date in qe_dates:
        if start_date <= qe_date <= end_date:
            closest_date = data.iloc[(data['Date'] - qe_date).abs().argmin()]['Date']
            closest_dates.append(closest_date)

    # Plot the data
    fig, ax1 = plt.subplots(figsize=(12, 6))

    ax1.plot(filtered_data['Date'], filtered_data['Brent Close'], label='Brent Futures', color='navy')
    ax1.set_xlabel('Date')
    ax1.set_ylabel('Brent Futures', color='navy')
    ax1.tick_params(axis='y', labelcolor='navy')
    ax1.yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, pos: f'{x:,.0f}'))

    ax2 = ax1.twinx()
    ax2.plot(filtered_data['Date'], filtered_data['EUR/USD'], label='EUR/USD', color='black')
    ax2.set_ylabel('EUR/USD', color='black')
    ax2.tick_params(axis='y', labelcolor='black')
    ax2.yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, pos: f'{x:,.2f}'))

    # Highlight QE announcement dates
    for date in closest_dates:
        ax1.axvline(x=date, color='red', linestyle='--', alpha=0.5)
    
    fig.suptitle(f'Brent Futures and EUR/USD ({start_date.date()} to {end_date.date()})')
    fig.tight_layout()

    # Save the plot as a PDF file to the desktop
    desktop_path = r"C:\Users\nsido\Desktop\Brent_EURUSD.pdf"
    plt.savefig(desktop_path)

    # Show the plot
    plt.show()

# Call the function to plot the data from 2012 to the end of 2014
plot_brent_eurusd('2008-01-01', '2025-04-30')
#%%
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from sklearn.linear_model import LinearRegression

# Set global font to Times New Roman
plt.rcParams["font.family"] = "Times New Roman"

# Load the data from the Excel file
file_path = 'C:\\Users\\nsido\\Desktop\\Graduate\\3. Masters - Summer 2024 (Reasearch Project)\\Analysis\\Figure Data_2024-07-19.xlsx'
sheet_name = 'Figure 3'
data = pd.read_excel(file_path, sheet_name=sheet_name)

# Parse dates and sort the data by date
data['Date'] = pd.to_datetime(data['Date'])
data.sort_values('Date', inplace=True)

# List of QE announcement dates
qe_dates = [
    '2008-11-25', '2008-12-01', '2008-12-16', '2009-03-18', '2009-08-12',
    '2009-09-23', '2009-11-04', '2010-08-10', '2010-11-03', '2011-09-21',
    '2012-09-13', '2012-12-12', '2013-12-18', '2020-03-15', '2020-03-23',
    '2020-06-10', '2021-11-03', '2021-12-15', '2022-01-26', '2024-05-01'
]
qe_dates = pd.to_datetime(qe_dates)

# Filter function to plot data within a specified date range
def plot_brent_eurusd(start_date, end_date):
    # Convert start_date and end_date to datetime format
    start_date = pd.to_datetime(start_date)
    end_date = pd.to_datetime(end_date)
    
    # Filter data within the specified date range
    filtered_data = data[(data['Date'] >= start_date) & (data['Date'] <= end_date)]

    # Find the closest dates in the data for each QE announcement date
    closest_dates = []
    for qe_date in qe_dates:
        if start_date <= qe_date <= end_date:
            closest_date = data.iloc[(data['Date'] - qe_date).abs().argmin()]['Date']
            closest_dates.append(closest_date)

    # Plot Brent Futures and EUR/USD on dual axes
    fig, ax1 = plt.subplots(figsize=(12, 6))

    ax1.plot(filtered_data['Date'], filtered_data['Brent Close'], label='Brent Futures', color='navy')
    ax1.set_xlabel('Date')
    ax1.set_ylabel('Brent Futures', color='navy')
    ax1.tick_params(axis='y', labelcolor='navy')
    ax1.yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, pos: f'{x:,.0f}'))

    ax2 = ax1.twinx()
    ax2.plot(filtered_data['Date'], filtered_data['EUR/USD'], label='EUR/USD', color='black')
    ax2.set_ylabel('EUR/USD', color='black')
    ax2.tick_params(axis='y', labelcolor='black')
    ax2.yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, pos: f'{x:,.2f}'))

    # Highlight QE announcement dates
    for date in closest_dates:
        ax1.axvline(x=date, color='red', linestyle='--', alpha=0.6, label='QE Announcements' if date == closest_dates[0] else "")

    fig.suptitle(f'Brent Futures and EUR/USD ({start_date.date()} to {end_date.date()})', fontsize=14)
    fig.tight_layout()

    # Save the plot as a PDF file to the desktop
    desktop_path = r"C:\Users\nsido\Desktop\Brent_EURUSD.pdf"
    plt.savefig(desktop_path)

    # Show the plot
    plt.show()

    # Correlation Plot
    plt.figure(figsize=(12, 6))

    # Scatter plot with a line of best fit
    x = filtered_data['Brent Close'].values.reshape(-1, 1)
    y = filtered_data['EUR/USD'].values
    model = LinearRegression()
    model.fit(x, y)
    predictions = model.predict(x)

    plt.scatter(x, y, color='navy', label='Data Points', alpha=0.6)
    plt.plot(x, predictions, color='black', linewidth=2, label='Fit Line')

    plt.xlabel('Brent Futures')
    plt.ylabel('EUR/USD')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()

    # Save the correlation plot as a PDF file to the desktop
    corr_plot_path = r"C:\Users\nsido\Desktop\Correlation_Brent_EURUSD.pdf"
    plt.savefig(corr_plot_path)

    # Show the correlation plot
    plt.show()

# Call the function to plot the data from 2008 to the end of 2014
plot_brent_eurusd('2008-11-01', '2008-12-30')

#%%
import pandas as pd
import matplotlib.pyplot as plt

# Set global font to Times New Roman
plt.rcParams["font.family"] = "Times New Roman"

# Load the data from the Excel file
file_path = 'C:\\Users\\nsido\\Desktop\\Graduate\\3. Masters - Summer 2024 (Reasearch Project)\\Analysis\\Figure Data_2024-07-19.xlsx'
sheet_name = 'Figure 3'
data = pd.read_excel(file_path, sheet_name=sheet_name)

# Parse dates and sort the data by date
data['Date'] = pd.to_datetime(data['Date'])
data.sort_values('Date', inplace=True)

# Calculate rolling correlation
window = 30  # Rolling window size (e.g., 30 days)
data['Rolling Correlation'] = data['Brent Close'].rolling(window=window).corr(data['EUR/USD'])

# Apply a moving average to smooth the rolling correlation
smoothing_window = 90  # Smoothing window size (e.g., 90 days)
data['Smoothed Correlation'] = data['Rolling Correlation'].rolling(window=smoothing_window).mean()

# Plot Rolling Correlation and Smoothed Correlation
plt.figure(figsize=(12, 6))
plt.plot(data['Date'], data['Rolling Correlation'], color='navy', alpha=0.5, label='Rolling Correlation (30 days)')
plt.plot(data['Date'], data['Smoothed Correlation'], color='black', linewidth=2, label='Smoothed Correlation (90 days)')
plt.xlabel('Date')
plt.ylabel('Correlation')
plt.title('Rolling Correlation between Brent Close and EUR/USD with Smoothing')
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()

# Save the plot as a PDF file to the desktop
smoothed_corr_path = r"C:\Users\nsido\Desktop\Smoothed_Rolling_Correlation_Brent_EURUSD.pdf"
plt.savefig(smoothed_corr_path)

# Show the plot
plt.show()
#%%
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Set global font to Times New Roman
plt.rcParams["font.family"] = "Times New Roman"

# Load the data from the Excel file
file_path = 'C:\\Users\\nsido\\Desktop\\Graduate\\3. Masters - Summer 2024 (Reasearch Project)\\Analysis\\Figure Data_2024-07-19.xlsx'
sheet_name = 'Figure 3'
data = pd.read_excel(file_path, sheet_name=sheet_name)

# Parse dates and sort the data by date
data['Date'] = pd.to_datetime(data['Date'])
data.sort_values('Date', inplace=True)

# Define rolling window sizes
windows = range(10, 91, 10)  # Rolling windows from 10 days to 90 days

# Initialize an empty list to store the results
results = []

# Compute rolling correlations for different window sizes
for window in windows:
    data['Rolling Brent'] = data['Brent Close'].rolling(window=window).mean()
    data['Rolling EUR/USD'] = data['EUR/USD'].rolling(window=window).mean()
    
    # Drop rows with NaN values
    data.dropna(subset=['Rolling Brent', 'Rolling EUR/USD'], inplace=True)
    
    # Calculate correlation
    correlation = data['Rolling Brent'].corr(data['Rolling EUR/USD'])
    results.append(correlation)

# Convert results to a DataFrame
results_df = pd.DataFrame(results, index=windows, columns=['Correlation'])

# Create the heatmap data
heatmap_data = pd.DataFrame(index=windows, columns=windows, dtype=float)

for window1 in windows:
    for window2 in windows:
        # Compute rolling correlation for window1 and window2
        data['Rolling Brent'] = data['Brent Close'].rolling(window=window1).mean()
        data['Rolling EUR/USD'] = data['EUR/USD'].rolling(window=window2).mean()
        data.dropna(subset=['Rolling Brent', 'Rolling EUR/USD'], inplace=True)
        correlation = data['Rolling Brent'].corr(data['Rolling EUR/USD'])
        heatmap_data.loc[window1, window2] = correlation

# Plot heatmap
plt.figure(figsize=(12, 8))
sns.heatmap(heatmap_data.astype(float), cmap='coolwarm', annot=True, fmt=".2f", linewidths=0.5)
plt.title('Heatmap of Rolling Correlation between Brent Close and EUR/USD')
plt.xlabel('Rolling Window Size for EUR/USD')
plt.ylabel('Rolling Window Size for Brent Close')
plt.tight_layout()

# Save the plot as a PDF file to the desktop
heatmap_path = r"C:\Users\nsido\Desktop\Heatmap_Rolling_Correlation_Brent_EURUSD.pdf"
plt.savefig(heatmap_path)

# Show the heatmap
plt.show()

