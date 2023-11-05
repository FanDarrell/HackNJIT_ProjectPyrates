# HackNJIT_ProjectPyrates
Project for the 2023 Fall NJIT Hackathon

Pyrates is based on a data set provided by https://github.com/newzealandpaul/Maritime-Pirate-Attacks/tree/v1.0/data/csv.
There are 3 csv files in this data set: Country codes, country indicators and pirate attacks in the countries along with various different statistics. In order to use this data in Python, we converted the csv files into dictionaries via the pandas library. We utilized the streamlit community cloud in order to upload the code for our website publicly.

Our project utilizes the streamlit and pandas in order to provide functionality to 3 separate tabs: Categorized Lists, Graphical Data and Attack Prediction Score

The Categorized Lists tab asks for you to give a way to sort the data: country, year, attack typem which will open a list right under it in which you can sort data accordingly.

The Graphical Data tab provides you with a bar graph and an interactive map that take data from the pirate_attacks csv. The bar graph sorts based on the category that the user chooses from the list. The interactive map shows red dots on the different parts of the maps

The Attack Prediction takes pirate_attacks.csv data and via machine learning we predicted the likeliness on a scale of 1-5 of the country speciifed by the user to be attacked by pirates.
