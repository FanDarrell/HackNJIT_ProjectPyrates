import streamlit as st
import pandas as pd
import streamlit.components.v1 as components

country_codes = pd.read_csv('https://raw.githubusercontent.com/FanDarrell/HackNJIT_ProjectPyrates/main/country_codes.csv')
country_indicators = pd.read_csv('https://raw.githubusercontent.com/FanDarrell/HackNJIT_ProjectPyrates/main/country_indicators.csv')
pirate_attacks = pd.read_csv('https://raw.githubusercontent.com/FanDarrell/HackNJIT_ProjectPyrates/main/pirate_attacks.csv')

st.title ='Pyrates'
st.header = 'Welcome to the Pyrates App!'

st.dataframe(country_codes)

#GET PIRATE ATTACKS BY NEAREST COUNTRY - CODE BY AM
cnames = country_codes[['country_name']]
option = st.selectbox(
    'Select A Country To View Pirate Attacks for that country:',
    (cnames))

st.write('You selected:', option)

#SELECT country_name WHERE country_name IS option
country_codes[country_codes['country_name'] == option]

#GET PIRATE ATTACKS BY ATTACK TYPE - BG
def attackTypeData():
    selected_option = st.selectbox('Select Attack Type:', ('N/A','Attempted', 'Boarded', 'Hijacked'))

    if selected_option is not 'N/A':
        pirate_attacks[pirate_attacks['attack_type'] == selected_option] 

attackTypeData()
