import streamlit as st
import pandas as pd
import streamlit.components.v1 as components


country_codes = pd.read_csv("https://raw.githubusercontent.com/FanDarrell/HackNJIT_ProjectPyrates/main/country_codes.csv")
country_indicators = pd.read_csv("https://raw.githubusercontent.com/FanDarrell/HackNJIT_ProjectPyrates/main/country_indicators.csv")
pirate_attacks = pd.read_csv("https://raw.githubusercontent.com/FanDarrell/HackNJIT_ProjectPyrates/main/pirate_attacks.csv")
temp = country_codes
country_dict = temp.set_index('country_name').T.to_dict('list')

st.title('Pyrates')
st.header('Welcome to the Pyrates App!')
#components.html(
##    """<link rel="stylesheet" href="pyrates.css">
#    """
#)

def years_only(x):
    return x.split('-')[0]

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
    st.subheader(f'Map of all pirate attacks in {date_to_filter}')
    st.map(filtered_data)
    


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



# Create a text element and let the reader know the data is loading.
data_load_state = st.text('Loading data...')
# Load 10,000 rows of data into the dataframe.
data = load_data(9000)
# Notify the reader that the data was successfully loaded.
data_load_state.text("Done! (using st.cache_data)")
map_show(data)
