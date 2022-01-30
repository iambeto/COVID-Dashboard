import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd

url_confirmed = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv'
url_deaths = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv'
url_recovered = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv'

confirmed = pd.read_csv(url_confirmed)
deaths = pd.read_csv(url_deaths)
recovered = pd.read_csv(url_recovered)

#unpivot data frames
date1 = confirmed.columns[4:]
total_confirmed = confirmed.melt(id_vars = ['Province/State', 'Country/Region', 'Lat', 'Long'], value_vars = date1, var_name = 'date', value_name = 'confirmed')
deaths = pd.read_csv(url_deaths)
date2 = deaths.columns[4:]
total_deaths = deaths.melt(id_vars = ['Province/State', 'Country/Region', 'Lat', 'Long'], value_vars = date2, var_name = 'date', value_name = 'deaths')
recovered = pd.read_csv(url_deaths)
date3 = recovered.columns[4:]
total_recovered = recovered.melt(id_vars = ['Province/State', 'Country/Region', 'Lat', 'Long'], value_vars = date3, var_name = 'date', value_name = 'recovered')

#merging data frames
covid_data = total_confirmed.merge(right = total_deaths, how = 'left', on = ['Province/State', 'Country/Region', 'date', 'Lat', 'Long'])
covid_data = covid_data.merge(right = total_recovered, how = 'left', on = ['Province/State', 'Country/Region', 'date', 'Lat', 'Long'])

#convert date column from string to proper format
covid_data['date'] = pd.to_datetime(covid_data['date'])

#check how many missing values NaN
covid_data.isna().sum()

#create new column
covid_data['active'] = covid_data['confirmed'] - covid_data['deaths'] - covid_data['recovered']

app = dash.Dash(__name__, )
app.layout = html.Div([

])

if __name__ == '__main__' :
    app.run_server(debug=True)






