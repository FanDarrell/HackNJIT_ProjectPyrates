import streamlit as st
import pandas as pd
import streamlit.components.v1 as components

#Create data frames for each CSV file.
country_codes = pd.read_csv("https://raw.githubusercontent.com/FanDarrell/HackNJIT_ProjectPyrates/main/country_codes.csv")
country_indicators = pd.read_csv("https://raw.githubusercontent.com/FanDarrell/HackNJIT_ProjectPyrates/main/country_indicators.csv")
pirate_attacks = pd.read_csv("https://raw.githubusercontent.com/FanDarrell/HackNJIT_ProjectPyrates/main/pirate_attacks.csv")
        


# Helper function for select__by_years() function. 
def years_only(x):
    return x.split('-')[0]

# Select by year function creates a selectbox that allows the user to get attacks by year. Code by SG
def select_by_year(df):
    df['date'] = df['date'].apply(years_only)
    year = st.selectbox('Select A Year To View Pirate Attacks for that Year:', df["date"].unique())
    st.write('You selected:', df.loc[df['date'] == year])

# Function that creates selectbox that allows user to get attacks by type. Code by SG & BG.
def select_by_attack(df):
    attack = st.selectbox('Select An Attack Type to View Attacks of that Type:', df["attack_type"].dropna().unique())
    st.write('You selected:', df.loc[df['attack_type'] == attack])

#st.dataframe(country_codes)

cnames = country_codes['country_name']
#st.dataframe(country_indicators)
#st.dataframe(pirate_attacks)
option = st.selectbox(
    'Select A Country To view Info:',
    (cnames))

''' Function that generates the options for sorting the data. Code by BG'''
    

##### MAIN DRIVER CODE ###
# Menu code that generates menu options that allows user to aggerate data based category. 
option = st.selectbox('Select how you would like to sort the data: ', ('', 'Country', 'Year', 'Attack Type'))

if option is 'Country':
    pass

if option is 'Year':
    select_by_year(pirate_attacks)

if option is 'Attack Type':
    select_by_attack(pirate_attacks)
