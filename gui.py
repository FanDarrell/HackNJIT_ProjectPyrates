import streamlit as st
import pandas as pd
import streamlit.components.v1 as components

st.title('Pyrates')
st.header('Welcome to the Pyrates Project!')

#Create data frames for each CSV file.
country_codes = pd.read_csv("https://raw.githubusercontent.com/FanDarrell/HackNJIT_ProjectPyrates/main/country_codes.csv")
country_indicators = pd.read_csv("https://raw.githubusercontent.com/FanDarrell/HackNJIT_ProjectPyrates/main/country_indicators.csv")
pirate_attacks = pd.read_csv("https://raw.githubusercontent.com/FanDarrell/HackNJIT_ProjectPyrates/main/pirate_attacks.csv")
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

def plot_attacks(df):
    plot_type = st.selectbox("Select A Category To Plot Number of Attacks by:", pirate_attacks.columns)
    #st.write("You selected:", plot_type)
    data = pd.DataFrame(df.value_counts(plot_type))
   # st.write(data)
    st.bar_chart(data)
 
# Menu code that generates menu options that allows user to aggerate data based category. Code by BG
option = st.selectbox('Select how you would like to sort the data: ', ('Select', 'Country', 'Year', 'Attack Type'))

if option is 'Country':
    select_by_country(pirate_attacks)

if option is 'Year':
    select_by_year(pirate_attacks)

if option is 'Attack Type':
    select_by_attack(pirate_attacks)
    plot_attacks(pirate_attacks)

st.divider()

#col1, col2, col3 , col4, col5 = st.beta_columns(5)

#with col1:
 #   pass
#with col2:
 #   pass
#with col4:
#    pass
#with col5:
 #   pass
#with col3 :
   # center_button = st.button('Check Your Ship\'s Risk Score!')

st.markdown('<center>', unsafe_allow_html=True)
st.button('Check Your Ship\'s Risk Score!')
st.markdown('</center>', unsafe_allow_html=True)
