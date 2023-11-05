import streamlit as st
import pandas as pd
import model.py as md
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
    date_to_filter = st.slider('date', 1993, 2020, 1993)
    filtered_data = data[data[DATE_COLUMN].dt.year == date_to_filter]
    st.subheader(f'Interactive map of all pirate attacks in {date_to_filter} [BETA]')
    st.map(filtered_data)

#EXPERIMENTAL - TABBED CONTAINER - Code by BG
tab1, tab2, tab3 = st.tabs(["Categorized Lists", "Graphical Data[BETA]", "Attack Prediction Score[BETA]"])    
 
with tab1:
    st.text('DESCRIPTION')
    # Menu code that generates menu options that allows user to aggerate data based category. Code by BG
    option = st.selectbox('Select how you would like to sort the data: ', ('Select', 'Country', 'Year', 'Attack Type'))
    
    if option is 'Country':
        select_by_country(pirate_attacks)

    if option is 'Year':
        select_by_year(pirate_attacks)

    if option is 'Attack Type':
        select_by_attack(pirate_attacks)
    
with tab2:
    st.text('DESCRIPTION')
    plot_attacks(pirate_attacks) #Load Graph Charts
    
    st.divider()
    # Load Map for Pirate Attack Locations:

    # Create a text element and let the reader know the data is loading.
    data_load_state = st.text('Loading data...')
    # Load 10,000 rows of data into the dataframe.
    data = load_data(9000)
    # Notify the reader that the data was successfully loaded.
    #data_load_state.text("Done! (using st.cache_data)")
    data_load_state.text('')
    map_show(data)

with tab3:
    st.text('DESCRIPTION')
    longtitude = st.text_input(
        'Enter Your Longtitude:',
        placeholder = 'Longtitude'
    )

    latitude = st.text_input(
        'Enter Your Latitude:',
        placeholder = 'Latitude'
    )

    model = md
    # predpiracy(self, long, lat)
    st.button('Generate Your Risk Score!', on_click =  md.predpiracy(self, longititude, latitude))
    #st.button('Generate Your Risk Score!')
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
st.link_button("Github Repo", "https://github.com/FanDarrell/HackNJIT_ProjectPyrates")
