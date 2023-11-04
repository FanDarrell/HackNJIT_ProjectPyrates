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

st.dataframe(country_codes)

option = st.selectbox(
    'Select A Country To View Pirate Attacks for that country:',
    ('USA', 'Finland', 'Somalia'))

st.write('You selected:', option)