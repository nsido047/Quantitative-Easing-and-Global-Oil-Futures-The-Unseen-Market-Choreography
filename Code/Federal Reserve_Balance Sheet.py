import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# Set global font to Times New Roman
plt.rcParams["font.family"] = "Times New Roman"

# Load the data from the Excel file
file_path = 'C:\\Users\\nsido\\Desktop\\Graduate\\3. Masters - Summer 2024 (Reasearch Project)\\Analysis\\Figure Data_2024-07-19.xlsx'
sheet_name = 'Figure 1'
data = pd.read_excel(file_path, sheet_name=sheet_name)

# Parse dates and sort the data by date
data['Date'] = pd.to_datetime(data['Date'])
data.sort_values('Date', inplace=True)

# Filter function to plot data within a specified date range
def plot_balance_sheet(start_date, end_date):
    # Convert start_date and end_date to datetime format
    start_date = pd.to_datetime(start_date)
    end_date = pd.to_datetime(end_date)
    
    # Filter data within the specified date range
    filtered_data = data[(data['Date'] >= start_date) & (data['Date'] <= end_date)]

    # List of QE announcement dates
    qe_dates = [
        '2008-11-25', '2008-12-01', '2008-12-16', '2009-03-18', '2009-08-12',
        '2009-09-23', '2009-11-04', '2010-08-10', '2010-11-03', '2011-09-21',
        '2012-09-13', '2012-12-12', '2013-12-18', '2020-03-15', '2020-03-23',
        '2020-06-10', '2021-11-03', '2021-12-15', '2022-01-26', '2024-05-01'
    ]

    # Convert QE announcement dates to datetime format
    qe_dates = pd.to_datetime(qe_dates)

    # Find the closest dates in the data for each QE announcement date
    closest_dates = []
    for qe_date in qe_dates:
        if start_date <= qe_date <= end_date:
            closest_date = data.iloc[(data['Date'] - qe_date).abs().argmin()]['Date']
            closest_dates.append(closest_date)

    # Plot the data
    plt.figure(figsize=(12, 6))
    plt.plot(filtered_data['Date'], filtered_data['Millions of U.S. Dollars'], label='Fed Balance Sheet')
    plt.scatter(closest_dates, data.loc[data['Date'].isin(closest_dates), 'Millions of U.S. Dollars'], color='red', label='QE Announcements')

    # Add labels and title
    plt.xlabel('Date')
    plt.ylabel('Fed Balance Sheet (Millions of U.S. Dollars)')
    plt.legend()

    # Highlight QE announcement dates
    for date in closest_dates:
        plt.axvline(x=date, color='red', linestyle='--', alpha=0.5)
    
    # Format the y-axis to make it more readable
    ax = plt.gca()
    ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, pos: f'{int(x):,}'))
    plt.xticks(rotation=45)
    plt.tight_layout()

    # Save the plot as a PDF file to the desktop
    desktop_path = r"C:\Users\nsido\Desktop\Fed Balance Sheet.pdf"
    plt.savefig(desktop_path)

    # Show the plot
    plt.show()

# Call the function to plot the data from 2008 to the end of 2010
plot_balance_sheet('2012-01-01', '2014-12-31')
