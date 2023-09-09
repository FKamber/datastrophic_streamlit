#############################################
# Kullanılacak Kütüphaneler
#############################################

import numpy as np
import pandas as pd
import seaborn as sns
import streamlit as st

import joblib
import pickle
import matplotlib.pyplot as plt


from ydata_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report
import pydeck as pdk
import plotly.express as px
from streamlit_option_menu import option_menu

#############################################
# Sayfaların Oluşumu
#############################################

st.set_page_config(
    page_title='DataStrophic2',
    layout="wide",
    page_icon="💰")

#st.sidebar.title("Navigation")
#page = st.sidebar.radio("Go to", ["Prediction", "EDA & Visualizations", "Contact"])

selected = option_menu("StartUp Project " , ["Predict", "Analysis", "Report", 'Communication'],
                        icons=['house', 'gear' , "list-task",'cloud-upload'],
                        menu_icon="cast", default_index=0, orientation="horizontal",
                        styles={
                            "container": {"padding": "0!important", "background-color": "#fafafa"},
                            "icon": {"color": "orange", "font-size": "25px"},
                            "nav-link": {"font-size": "25px", "text-align": "left", "margin": "0px",
                                         "--hover-color": "#eee"},
                            "nav-link-selected": {"background-color": "green"}})
selected



