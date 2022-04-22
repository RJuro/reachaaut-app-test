import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt #plot control
sns.set() #plot style


st.set_page_config(page_title='ReachAAUt workshop',
page_icon="🚀",
layout='wide'
)

# LOAD DATA ONCE
@st.experimental_singleton
def load_data():

    data = pd.read_csv('https://github.com/RJuro/reachaaut-workshops/raw/main/cph-listings.gz')

    data = data[data.number_of_reviews > 0]
    data = data[data.room_type.isin(['Private room', 'Entire home/apt'])]
    data['price_z'] = (data['price'] - data['price'].mean())/data['price'].std(ddof=0)
    data['price_z'] = data['price_z'].abs()
    data = data[data.price_z < 3]
    data['log_price'] = np.log(data['price'])

    return data

data = load_data()




st.title("AirBnb rentals in Copenhagen 🇩🇰")

st.text("""This is some text describing a very complex project....
"""
)

countplot = plt.figure()
sns.countplot(y="neighbourhood", 
                hue="room_type", 
                data=data, 
                order = data.neighbourhood.value_counts().index)

st.pyplot(countplot)
