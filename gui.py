import streamlit as st
import pandas as pd
from model import Model
import streamlit.components.v1 as components

#Created by: Amrit Madabushi, Brandon Green, Dan Farrell and Saketh Golla

st.title(':snake: Pyrates :pirate_flag:')
st.header('Welcome to the Pyrates Project!')

st.divider()
st.text('An app that lets you view historical data on real life pirate attacks, as well as\n lets you see how likely you are to be hijacked by pirates using our state of \nthe art Machine Learning Algorithm! ')
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
    df['date'] = df['date'].apply(years_only)
    plot_type = st.selectbox("Select A Category To Plot Number of Attacks by:", ('nearest_country', 'date', 'attack_type', 'vessel_type', 'vessel_status'))
    #st.write("You selected:", plot_type)
    data = df.value_counts(plot_type).to_frame()
    data[plot_type] = data.index
    st.header("Count of pirate attacks by " + plot_type)
    st.divider()
    st.bar_chart(data, x=plot_type, y="count")

#Map Of Pirate Attack Locations - Code by AM
@st.cache_data
def load_data(nrows):
    DATE_COLUMN = 'date'
    DATA_URL = 'https://raw.githubusercontent.com/FanDarrell/HackNJIT_ProjectPyrates/main/pirate_attacks.csv'
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data


def map_show(data):
    DATE_COLUMN = 'date'
    DATA_URL = 'https://raw.githubusercontent.com/FanDarrell/HackNJIT_ProjectPyrates/main/pirate_attacks.csv'
    date_to_filter = 1993
    date_to_filter = st.slider('date', min_value=1993, max_value=2020, value=1993, key="slider")
    filtered_data = data[data[DATE_COLUMN].dt.year == date_to_filter]
    st.subheader(f'Interactive map of all pirate attacks in {date_to_filter} [BETA]')
    st.map(filtered_data)

#Function that calls the Machine Learning Model in the UI based on the latitude and longitude the user enters. Code by DF and SG
def callModel(latitude, longitude):
    md = Model()
    try:
        result = md.predpiracy(longitude, latitude)
        st.write("Your piracy risk score is: " + str(round(result[0],2)))
        if(result[0] < 3):
            st.write(":green[You are safe from pirate attacks!]")
        elif(result[0] >= 3):
            st.write(":red[You are at a high risk of pirate attacks!]")
    except ValueError:
        st.write("Please enter a valid latitude and longitude")
    pass

#EXPERIMENTAL - TABBED CONTAINER - Code by BG
tab1, tab2, tab3 = st.tabs(["Categorized Lists", "Graphical Data[BETA]", "Attack Prediction Score[BETA]"])    
 
with tab1:
    st.text('Select a category from the dropdown menu to see a list of pirates \nattacks in that category.')
    # Menu code that generates menu options that allows user to aggerate data based category. Code by BG
    option = st.selectbox('Select how you would like to sort the data: ', ('Select', 'Country', 'Year', 'Attack Type'))
    
    if option is 'Country':
        select_by_country(pirate_attacks)

    if option is 'Year':
        select_by_year(pirate_attacks)

    if option is 'Attack Type':
        select_by_attack(pirate_attacks)
    
with tab2:
    plot_attacks(pirate_attacks) #Load Graph Charts
    
    st.divider()
    # Load Map for Pirate Attack Locations:

    # Create a text element and let the reader know the data is loading.
    data_load_state = st.text('Loading data...')
    # Load 10,000 rows of data into the dataframe.
    data = load_data(9000)
    data_load_state.text('') #BUGFIX to keep 'Loading data...' message from remaining on screen after data is loaded.
    map_show(data)

with tab3:
    st.text('Choose a coordinate pair to recieve a piracy score which indicates \nhow at risk a ship would be at the chosen location.')
    longitude = st.text_input(
        'Enter Your Longitude:',
        placeholder = 'Longitude'
    )

    latitude = st.text_input(
        'Enter Your Latitude:',
        placeholder = 'Latitude'
    )
    st.button('Generate Your Risk Score!', on_click=callModel(latitude, longitude))

st.divider()
st.text('App Created @ HackNJIT 2023 by team Pyrates.')
st.text('Pyrates Team Members: Amrit Madabushi, Brandon Green, Dan Farrell and Saketh Golla ')
st.link_button("Github Repo", "https://github.com/FanDarrell/HackNJIT_ProjectPyrates")
