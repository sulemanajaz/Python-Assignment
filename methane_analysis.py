import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#file name of the World bank data file
file_name = 'world_bank_data.csv'

# Defining the function which takes a filename as argument, reads a dataframe in World bank format and 
# returns three dataframes: Countries list dataframes, Years list dataframes and master dataframes.
def process_data(data_in):

    data = pd.read_csv(data_in,on_bad_lines='skip',skiprows=4)
    df_countries = data["Country Name"].unique()
    df_years = data.columns[4:]
    
    return df_countries,df_years,data

# Calling the function process_data
countries_list,years_list,data=process_data(file_name)

#List of Years choosen for data visualization
years_choosen = ['1990', '1995', '2000', '2005', '2010', '2015', '2020']


#List of Countries choosen for data visualization
countries_choosen = ['Bangladesh','Brazil','Canada','China','Ecuador','France','India','Nigeria','South Africa','Sweden','United Kingdom','United States']

#Defining function to fetch the data for Methane emissions (kt of CO2 equivalent) from the master data frame
def fetch_process():

    fetch_data=[]
    years=[]
    countries=[]
    
    for year in years_choosen:
        for country in countries_choosen:
            years.append(year)
            countries.append(country)
            fetch_data.append(data[year][(data['Indicator Name'] == 'Methane emissions (kt of CO2 equivalent)') & (data['Country Name']==country)].to_string(index=False))
    
    initial_data = {
                'Year': years,
                'Country': countries,
                'Methane emissions (kt of CO2 equivalent)':fetch_data
               }

    processed_data = pd.DataFrame(initial_data, columns = ['Year','Country','Methane emissions (kt of CO2 equivalent)'])
    
    return processed_data

# Calling the function fetch_process
fetch_data = fetch_process()


data1=[]
data2=[]
data3=[]
data4=[]
data5=[]
data6=[]
data7=[]
data8=[]
data9=[]
data10=[]
data11=[]
data12=[]

for year in years_choosen:
    data1.append(float(fetch_data['Methane emissions (kt of CO2 equivalent)'][(fetch_data['Country']=='Bangladesh') & (fetch_data['Year']==year)].to_string(index=False)))

for year in years_choosen:
    data2.append(float(fetch_data['Methane emissions (kt of CO2 equivalent)'][(fetch_data['Country']=='Brazil') & (fetch_data['Year']==year)].to_string(index=False)))

for year in years_choosen:
    data3.append(float(fetch_data['Methane emissions (kt of CO2 equivalent)'][(fetch_data['Country']=='Canada') & (fetch_data['Year']==year)].to_string(index=False)))

for year in years_choosen:
    data4.append(float(fetch_data['Methane emissions (kt of CO2 equivalent)'][(fetch_data['Country']=='China') & (fetch_data['Year']==year)].to_string(index=False)))

for year in years_choosen:
    data5.append(float(fetch_data['Methane emissions (kt of CO2 equivalent)'][(fetch_data['Country']=='Ecuador') & (fetch_data['Year']==year)].to_string(index=False)))

for year in years_choosen:
    data6.append(float(fetch_data['Methane emissions (kt of CO2 equivalent)'][(fetch_data['Country']=='France') & (fetch_data['Year']==year)].to_string(index=False)))

for year in years_choosen:
    data7.append(float(fetch_data['Methane emissions (kt of CO2 equivalent)'][(fetch_data['Country']=='India') & (fetch_data['Year']==year)].to_string(index=False)))

for year in years_choosen:
    data8.append(float(fetch_data['Methane emissions (kt of CO2 equivalent)'][(fetch_data['Country']=='Nigeria') & (fetch_data['Year']==year)].to_string(index=False)))

for year in years_choosen:
    data9.append(float(fetch_data['Methane emissions (kt of CO2 equivalent)'][(fetch_data['Country']=='South Africa') & (fetch_data['Year']==year)].to_string(index=False)))

for year in years_choosen:
    data10.append(float(fetch_data['Methane emissions (kt of CO2 equivalent)'][(fetch_data['Country']=='Sweden') & (fetch_data['Year']==year)].to_string(index=False)))

for year in years_choosen:
    data11.append(float(fetch_data['Methane emissions (kt of CO2 equivalent)'][(fetch_data['Country']=='United Kingdom') & (fetch_data['Year']==year)].to_string(index=False)))

for year in years_choosen:
    data12.append(float(fetch_data['Methane emissions (kt of CO2 equivalent)'][(fetch_data['Country']=='United States') & (fetch_data['Year']==year)].to_string(index=False)))

    
# Setting the width and height for the plot - width:10, height:10
plt.figure(figsize=(10,10)) 

plt.plot(years_choosen, data1, label = "Bangladesh")
plt.plot(years_choosen, data2, label = "Brazil")
plt.plot(years_choosen, data3, label = "Canada")
plt.plot(years_choosen, data4, label = "China")
plt.plot(years_choosen, data5, label = "Ecuador")
plt.plot(years_choosen, data6, label = "France")
plt.plot(years_choosen, data7, label = "India")
plt.plot(years_choosen, data8, label = "Nigeria")
plt.plot(years_choosen, data9, label = "South Africa")
plt.plot(years_choosen, data10, label = "Sweden")
plt.plot(years_choosen, data11, label = "United Kingdom")
plt.plot(years_choosen, data12, label = "United States")

# naming the x axis
plt.xlabel('Year')

# naming the y axis
plt.ylabel('Methane emissions (kt of CO2 equivalent)')

# giving a title to the plot
plt.title('Methane emissions across the world (1990 - 2020)')
  
# show a legend on the plot
plt.legend(title="Year", loc='upper left',bbox_to_anchor=(1,1))
  
# function to show the plot
plt.show()