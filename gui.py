import streamlit as st
import pandas as pd
import streamlit.components.v1 as components

country_codes = pd.read_csv("https://raw.githubusercontent.com/FanDarrell/HackNJIT_ProjectPyrates/main/country_codes.csv")
country_indicators = pd.read_csv("https://raw.githubusercontent.com/FanDarrell/HackNJIT_ProjectPyrates/main/country_indicators.csv")
pirate_attacks = pd.read_csv("https://raw.githubusercontent.com/FanDarrell/HackNJIT_ProjectPyrates/main/pirate_attacks.csv")


#components.html(
##    """<link rel="stylesheet" href="pyrates.css">
#    """
#)

st.title ="Pyrates"
st.header = "Welcome to the Pyrates App!"

#displays the entire csv file
st.dataframe(country_codes)

#Names of the countries
cnames = country_codes[['country_name']]
st.dataframe(country_indicators)
st.dataframe(pirate_attacks)
option = st.selectbox(
    'Select A Country To view Info:',
    (cnames))

st.write('You selected:', option)

country_codes[country_codes['country_name'] == option]

#represents the value of the country code from the country name
code = country_codes.loc[country_codes['country_name'] == option, ['country']].values[0]
country_codes.loc[country_codes.at['country_name'] == option, ['country']][0]
#country_codes.at[option, 'country']
#country_codes[['country']]
#pirate_attacks[['nearest_country']]
#pirate_attacks.loc[pirate_attacks['nearest_country'] == code]