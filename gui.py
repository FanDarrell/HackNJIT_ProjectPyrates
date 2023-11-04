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

def years_only(x):
    return x.split('-')[0]

# select by year function creates a selectbox that allows the user to select a year to filter attacks by
def select_by_year(df):
    year = st.selectbox('Select A Year To View Pirate Attacks for that Year:', df["date"].unique())
    st.write('You selected:', df.loc[df['date'] == year])

def select_by_attack(df):
    attack = st.selectbox('Select An Attack Type to View Attacks of that Type:', df["attack_type"].unique())
    st.write('You selected:', df.loc[df['attack_type'] == attack])

st.title ="Pyrates"
st.header = "Welcome to the Pyrates App!"

st.dataframe(country_codes)

cnames = country_codes['country_name']
st.dataframe(country_indicators)
st.dataframe(pirate_attacks)
option = st.selectbox(
    'Select A Country To view Info:',
    (cnames))

#calling the select by year function 
pirate_attacks['date'] = pirate_attacks['date'].apply(years_only)
select_by_year(pirate_attacks)

#calling the select by attack function
select_by_attack(pirate_attacks)