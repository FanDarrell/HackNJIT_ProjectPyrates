import streamlit as st
import pandas as pd
import streamlit.components.v1 as components


st.title(':snake: Pyrates :pirate_flag:')
st.header('Welcome to the Pyrates Project!')

#Create data frames for each CSV file.
country_codes = pd.read_csv("https://raw.githubusercontent.com/FanDarrell/HackNJIT_ProjectPyrates/main/country_codes.csv")
country_indicators = pd.read_csv("https://raw.githubusercontent.com/FanDarrell/HackNJIT_ProjectPyrates/main/country_indicators.csv")
pirate_attacks = pd.read_csv("https://raw.githubusercontent.com/FanDarrell/HackNJIT_ProjectPyrates/main/pirate_attacks.csv")

#BUGFIX for getting country code using country name. Code by SG.
temp = country_codes
country_dict = temp.set_index('country_name').T.to_dict('list')

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

def select_by_country(df):
    country = st.selectbox('Select A Country To View Pirate Attacks for that Country:', country_codes['country_name'])
    st.write("You selected:", df.loc[df['nearest_country'] == country_dict[country][0]])

#EXPERIMENTAL GRAPH CHARTS. CODE BY SG
def plot_attacks(df):
    plot_type = st.selectbox("Select A Category To Plot Number of Attacks by:", pirate_attacks.columns)
    #st.write("You selected:", plot_type)
    data = pd.DataFrame(df.value_counts(plot_type))
   # st.write(data)
    st.bar_chart(data)

#EXPERIMENTAL - TABBED CONTAINER - Code by BG
tab1, tab2, tab3 = st.tabs(["Categorized Lists", "Graphical Data[BETA]", "Attack Prediction Score[BETA]"])    
 
with tab1:
    st.text('DESCRIPTION')
    # Menu code that generates menu options that allows user to aggerate data based category. Code by BG
    option = st.selectbox('Select how you would like to sort the data: ', ('Select', 'Country', 'Year', 'Attack Type'))

with tab2:
    st.text('DESCRIPTION')
    plot_attacks(pirate_attacks)

with tab3:
    st.text('DESCRIPTION')
    latitude = st.text_input(
        'Enter Your Latitude:',
        placeholder = 'Latitude'
    )

    longtitude = st.text_input(
        'Enter Your Longtitude:',
        placeholder = 'Longtitude'
    )
    st.button('Generate Your Risk Score!')
if option is 'Country':
    select_by_country(pirate_attacks)

if option is 'Year':
    select_by_year(pirate_attacks)

if option is 'Attack Type':
    select_by_attack(pirate_attacks)
    #plot_attacks(pirate_attacks)

# Menu code that generates menu options that allows user to aggerate data based category. Code by BG
#option = st.selectbox('Select how you would like to sort the data: ', ('Select', 'Country', 'Year', 'Attack Type'))

#if option is 'Country':
#    select_by_country(pirate_attacks)

#if option is 'Year':
 #   select_by_year(pirate_attacks)

#if option is 'Attack Type':
 #   select_by_attack(pirate_attacks)
 #   plot_attacks(pirate_attacks)

st.divider()
st.text('App Created @ HackNJIT 2023 by team Pyrates.')
st.text('Pyrates Team Members: Amrit Madabushi, Brandon Green, Dan Farrell and Saketh G. ')

