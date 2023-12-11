import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

#file name of the World bank data file
file_name = 'world_bank_data.csv'

# Defining the function which takes a filename as an argument, reads a dataframe in World bank format, 
# and returns three dataframes: Countries list dataframes, Years list dataframes, and master dataframes.
def process_data(data_in):
    data = pd.read_csv(data_in, on_bad_lines='skip', skiprows=4)
    df_countries = data["Country Name"].unique()
    df_years = data.columns[4:]
    return df_countries, df_years, data

# Calling the function process_data
countries_list, years_list, data = process_data(file_name)

# List of Years chosen for data visualization
years_choosen = ['1990', '1995', '2000', '2005', '2010', '2015', '2020']

# List of Countries chosen for data visualization
countries_choosen = ['Bangladesh', 'Brazil', 'Canada', 'China', 'Ecuador', 'France', 'India', 'Nigeria', 'South Africa', 'Sweden', 'United Kingdom', 'United States']

# Defining function to fetch the data for Population growth (annual %) from the master data frame
def fetch_process(data):
    fetch_details = []
    years = []
    countries = []

    for year in years_choosen:
        for country in countries_choosen:
            years.append(year)
            countries.append(country)
            fetch_details.append(data[year][(data['Indicator Name'] == 'Population growth (annual %)') & (data['Country Name'] == country)].to_string(index=False))

    initial_data = {
        'Year': years,
        'Country': countries,
        'Population growth (annual %)': fetch_details
    }

    processed_data = pd.DataFrame(initial_data, columns=['Year', 'Country', 'Population growth (annual %)'])

    return processed_data

# Calling the function fetch_process
fetch_data = fetch_process(data)

data1 = []
data2 = []
data3 = []
data4 = []
data5 = []
data6 = []
data7 = []

for country in countries_choosen:
    data1.append(float(fetch_data['Population growth (annual %)'][(fetch_data['Country'] == country) & (fetch_data['Year'] == '1990')].to_string(index=False)))

for country in countries_choosen:
    data2.append(float(fetch_data['Population growth (annual %)'][(fetch_data['Country'] == country) & (fetch_data['Year'] == '1995')].to_string(index=False)))

for country in countries_choosen:
    data3.append(float(fetch_data['Population growth (annual %)'][(fetch_data['Country'] == country) & (fetch_data['Year'] == '2000')].to_string(index=False)))

for country in countries_choosen:
    data4.append(float(fetch_data['Population growth (annual %)'][(fetch_data['Country'] == country) & (fetch_data['Year'] == '2005')].to_string(index=False)))

for country in countries_choosen:
    data5.append(float(fetch_data['Population growth (annual %)'][(fetch_data['Country'] == country) & (fetch_data['Year'] == '2010')].to_string(index=False)))

for country in countries_choosen:
    data6.append(float(fetch_data['Population growth (annual %)'][(fetch_data['Country'] == country) & (fetch_data['Year'] == '2015')].to_string(index=False)))

for country in countries_choosen:
    data7.append(float(fetch_data['Population growth (annual %)'][(fetch_data['Country'] == country) & (fetch_data['Year'] == '2020')].to_string(index=False)))


# Creating a DataFrame with the collected population growth data
heatmap_data = pd.DataFrame({
    'Country': countries_choosen * len(years_choosen),
    'Year': sorted(years_choosen * len(countries_choosen)),
    'Population Growth': data1 + data2 + data3 + data4 + data5 + data6 + data7
})

# Pivot the DataFrame for heatmap visualization
heatmap_data_pivot = heatmap_data.pivot(index='Country', columns='Year', values='Population Growth')

# Plotting the heatmap
plt.figure(figsize=(10, 7))
sns.heatmap(heatmap_data_pivot, cmap='viridis', annot=True, linewidths=.5)

plt.title('Annual Population Growth around the world (1990 - 2020)')

# Display the heatmap
plt.show()
