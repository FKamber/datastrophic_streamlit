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

if selected == "Predict":
    st.title("StartUp Prediction")

    # Modeli yükleyin
    # Modelin tam yolunu kullanarak modeli yükleyin
    model_path = 'ml_features_df.joblib'
    model = joblib.load(model_path)


    # Kullanıcıdan girdi alacağız
    # Özellikleri belirtin ve değerlerini isteyin

    st.sidebar.title("Navigation")

    # Collects user input features into dataframe
    #uploaded_file = st.sidebar.file_uploader("Upload your input CSV file", type=["csv"])
    #if uploaded_file is not None:
        #input_df = pd.read_csv(uploaded_file)
    def user_input_features():

        market_val = st.sidebar.selectbox('market', ('Publishing','Electronics','Tourism'
                                                     'Software','Biotechnology','Education'))
        funding_total_usd_val = st.sidebar.number_input('funding_total_usd', min_value=0, step=1)
        status_val = st.sidebar.radio("Status",('Acquired', 'Closed', 'Operating'))
        seed_val = st.sidebar.radio("seed",('Acquired', 'Closed', 'Operating'))
        venture_val = st.sidebar.radio("venture",('Acquired', 'Closed', 'Operating'))
        equity_crowdfunding_val = st.sidebar.radio("equity_crowdfunding",('Acquired', 'Closed', 'Operating'))
        undisclosed_val = st.sidebar.radio("undisclosed",('Acquired', 'Closed', 'Operating'))
        convertible_note_val = st.sidebar.radio("convertible_note",('Acquired', 'Closed', 'Operating'))
        debt_financing_val = st.sidebar.radio("debt_financing",('Acquired', 'Closed', 'Operating'))
        angel_val = st.sidebar.radio("angel", ('Acquired', 'Closed', 'Operating'))
        grant_val = st.sidebar.radio("grant", ('Acquired', 'Closed', 'Operating'))
        private_equity_val = st.sidebar.radio("private_equity", ('Acquired', 'Closed', 'Operating'))
        post_ipo_equity_val = st.sidebar.radio("post_ipo_equity", ('Acquired', 'Closed', 'Operating'))
        post_ipo_debt_val = st.sidebar.radio("post_ipo_debt", ('Acquired', 'Closed', 'Operating'))
        secondary_market_val = st.sidebar.radio("secondary_market", ('Acquired', 'Closed', 'Operating'))
        product_crowdfunding_val = st.sidebar.radio("product_crowdfunding", ('Acquired', 'Closed', 'Operating'))
        round_A_val = st.sidebar.radio("round_A", ('Acquired', 'Closed', 'Operating'))
        round_B_val = st.sidebar.radio("round_B", ('Acquired', 'Closed', 'Operating'))
        round_C_val = st.sidebar.radio("round_C", ('Acquired', 'Closed', 'Operating'))
        round_D_val = st.sidebar.radio("round_D", ('Acquired', 'Closed', 'Operating'))
        round_E_val = st.sidebar.radio("round_E", ('Acquired', 'Closed', 'Operating'))
        round_F_val = st.sidebar.radio("round_F", ('Acquired', 'Closed', 'Operating'))
        round_G_val = st.sidebar.radio("round_G", ('Acquired', 'Closed', 'Operating'))
        round_H_val = st.sidebar.radio("round_H", ('Acquired', 'Closed', 'Operating'))
        country_val = st.sidebar.radio("country", ('Acquired', 'Closed', 'Operating'))
        diff_funding_months_val = st.sidebar.radio("diff_funding_months", ('Acquired', 'Closed', 'Operating'))
        diff_first_funding_months_val = st.sidebar.radio("diff_first_funding_months", ('Acquired', 'Closed', 'Operating'))
        round_A_H_total_val = st.sidebar.radio("round_A_H_total", ('Acquired', 'Closed', 'Operating'))
        angel_status_val = st.sidebar.radio("angel_status", ('Acquired', 'Closed', 'Operating'))
        grant_status_val = st.sidebar.radio("grant_status", ('Acquired', 'Closed', 'Operating'))
        avg_fund_size_val = st.sidebar.radio("avg_fund_size", ('Acquired', 'Closed', 'Operating'))
        ratio_seed_tot_val = st.sidebar.radio("ratio_seed_tot", ('Acquired', 'Closed', 'Operating'))
        ratio_debt_tot_val = st.sidebar.radio("ratio_debt_tot", ('Acquired', 'Closed', 'Operating'))
        convertible_status_val = st.sidebar.radio("convertible_status", ('Acquired', 'Closed', 'Operating'))
        seed_quartiles_val = st.sidebar.radio("seed_quartiles", ('Acquired', 'Closed', 'Operating'))
        angel_degree_val = st.sidebar.radio("angel_degree", ('Acquired', 'Closed', 'Operating'))
        tot_funding_degree_val = st.sidebar.radio("tot_funding_degree", ('Acquired', 'Closed', 'Operating'))
        venture_degree_val = st.sidebar.radio("venture_degree", ('Acquired', 'Closed', 'Operating'))
        start_postion_val = st.sidebar.radio("start_postion", ('Acquired', 'Closed', 'Operating'))
        secondary_status_val = st.sidebar.radio("secondary_status", ('Acquired', 'Closed', 'Operating'))
        recency_val = st.sidebar.radio("recency", ('Acquired', 'Closed', 'Operating'))

        data = {'market': market_val,
                'funding_total_usd': funding_total_usd_val,
                'status': status_val,
                'seed': seed_val,
                'venture': venture_val,
                'equity_crowdfunding': equity_crowdfunding_val,
                'undisclosed': undisclosed_val,
                'convertible_note': convertible_note_val,
                'debt_financing': debt_financing_val,
                'angel': angel_val,
                'grant': grant_val,
                'private_equity': private_equity_val,
                'post_ipo_equity': post_ipo_equity_val,
                'post_ipo_debt': post_ipo_debt_val,
                'secondary_market': secondary_market_val,
                'product_crowdfunding': product_crowdfunding_val,
                'round_A': round_A_val,
                'round_B': round_B_val,
                'round_C': round_C_val,
                'round_D': round_D_val,
                'round_E': round_E_val,
                'round_F': round_F_val,
                'round_G': round_G_val,
                'round_H': round_H_val,
                'country': country_val,
                'diff_funding_months': diff_funding_months_val,
                'diff_first_funding_months': diff_first_funding_months_val,
                'round_A_H_total': round_A_H_total_val,
                'angel_status': angel_status_val,
                'grant_status': grant_status_val,
                'avg_fund_size': avg_fund_size_val,
                'ratio_seed_tot': ratio_seed_tot_val,
                'ratio_debt_tot': ratio_debt_tot_val,
                'convertible_status': convertible_status_val,
                'seed_quartiles': seed_quartiles_val,
                'angel_degree': angel_degree_val,
                'tot_funding_degree': tot_funding_degree_val,
                'venture_degree': venture_degree_val,
                'start_postion': start_postion_val,
                'secondary_status': secondary_status_val,
                'recency': recency_val}

        features = pd.DataFrame(data, index=[0])
        return features

    input_df = user_input_features()

    st.dataframe(input_df)

