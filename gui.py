import streamlit as st
import pandas as pd
import streamlit.components.v1 as components

country_codes = pd.read_csv("https://raw.githubusercontent.com/FanDarrell/HackNJIT_ProjectPyrates/main/country_codes.csv")
country_indicators = pd.read_csv("https://raw.githubusercontent.com/FanDarrell/HackNJIT_ProjectPyrates/main/country_indicators.csv")
pirate_attacks = pd.read_csv("https://raw.githubusercontent.com/FanDarrell/HackNJIT_ProjectPyrates/main/pirate_attacks.csv")
temp = country_codes
country_dict = temp.set_index('country_name').T.to_dict('list')

#components.html(
##    """<link rel="stylesheet" href="pyrates.css">
#    """
#)
st.title(':snake: Pyrates :pirate_flag:')
st.header('Welcome to the Pyrates Project!')

def years_only(x):
    return x.split('-')[0]

def val_counts(x):
    return x.value_counts()

# select by year function creates a selectbox that allows the user to select a year to filter attacks by
def select_by_year(df):
    df['date'] = df['date'].apply(years_only)
    year = st.selectbox('Select A Year To View Pirate Attacks for that Year:', df["date"].unique())
    st.write('You selected:', df.loc[df['date'] == year])

def select_by_attack(df):
    attack = st.selectbox('Select An Attack Type to View Attacks of that Type:', df["attack_type"].dropna().unique())
    st.write('You selected:', df.loc[df['attack_type'] == attack])

def select_by_country(df):
    country = st.selectbox('Select A Country To View Pirate Attacks for that Country:', country_codes['country_name'])
    st.write("You selected:", df.loc[df['nearest_country'] == country_dict[country][0]])

def plot_attacks(df):
    plot_type = st.selectbox("Select A Category To Plot Number of Attacks by:", pirate_attacks.columns)
    st.write("You selected:", plot_type)
    data = pd.DataFrame(df.value_counts(plot_type))
    st.write(data)
    st.bar_chart(data)

st.dataframe(country_codes)

#cnames = country_codes['country_name']
st.dataframe(country_indicators)
st.dataframe(pirate_attacks)
# option = st.selectbox(
#   'Select A Country To view Info:',
#    (cnames))


#calling the select by year function 
select_by_year(pirate_attacks)
#calling the select by attack function
select_by_attack(pirate_attacks)
#calling the select by country function
select_by_country(pirate_attacks)
#calling the plot function
plot_attacks(pirate_attacks)
