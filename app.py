#############################################
# Kullanılacak Kütüphaneler
#############################################

import numpy as np
import pandas as pd
import seaborn as sns
import streamlit as st

import pickle


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
    #model_path = 'pickle_clean_crunchbase.pkl'
    #model = pickle.load(model_path)

    with open('pickle_clean_crunchbase.pkl', 'rb') as file:
        model = pickle.load(file)


    # Kullanıcıdan girdi alacağız
    # Özellikleri belirtin ve değerlerini isteyin

    st.sidebar.title("Navigation")

    # Collects user input features into dataframe
    #uploaded_file = st.sidebar.file_uploader("Upload your input CSV file", type=["csv"])
    #if uploaded_file is not None:
        #input_df = pd.read_csv(uploaded_file)
    def user_input_features():

        market_mm = st.sidebar.selectbox('market', ('Publishing','Electronics','Tourism'
                                                     'Software','Biotechnology','Education'))
        funding_total_usd_mm = st.sidebar.number_input('funding_total_usd', step=1)
        status_mm = st.sidebar.radio("Status",('Acquired', 'Closed', 'Operating'))
       # seed_mm = st.sidebar.radio("seed",('Acquired', 'Closed', 'Operating'))
        venture_mm = st.sidebar.radio("venture",('Acquired', 'Closed', 'Operating'))
        equity_crowdfunding_mm = st.sidebar.radio("equity_crowdfunding",('Acquired', 'Closed', 'Operating'))
        undisclosed_mm = st.sidebar.radio("undisclosed",('Acquired', 'Closed', 'Operating'))
        convertible_note_mm = st.sidebar.radio("convertible_note",('Acquired', 'Closed', 'Operating'))
        debt_financing_mm = st.sidebar.radio("debt_financing",('Acquired', 'Closed', 'Operating'))
        angel_mm = st.sidebar.radio("angel", ('Acquired', 'Closed', 'Operating'))
        grant_mm = st.sidebar.radio("grant", ('Acquired', 'Closed', 'Operating'))
        private_equity_mm = st.sidebar.radio("private_equity", ('Acquired', 'Closed', 'Operating'))
        post_ipo_equity_mm = st.sidebar.radio("post_ipo_equity", ('Acquired', 'Closed', 'Operating'))
        post_ipo_debt_mm = st.sidebar.radio("post_ipo_debt", ('Acquired', 'Closed', 'Operating'))
        secondary_market_mm = st.sidebar.radio("secondary_market", ('Acquired', 'Closed', 'Operating'))
        product_crowdfunding_mm = st.sidebar.radio("product_crowdfunding", ('Acquired', 'Closed', 'Operating'))
        round_A_mm = st.sidebar.radio("round_A", ('Acquired', 'Closed', 'Operating'))
        round_B_mm = st.sidebar.radio("round_B", ('Acquired', 'Closed', 'Operating'))
        round_C_mm = st.sidebar.radio("round_C", ('Acquired', 'Closed', 'Operating'))
        round_D_mm = st.sidebar.radio("round_D", ('Acquired', 'Closed', 'Operating'))
        round_E_mm = st.sidebar.radio("round_E", ('Acquired', 'Closed', 'Operating'))
        round_F_mm = st.sidebar.radio("round_F", ('Acquired', 'Closed', 'Operating'))
        round_G_mm = st.sidebar.radio("round_G", ('Acquired', 'Closed', 'Operating'))
        round_H_mm = st.sidebar.radio("round_H", ('Acquired', 'Closed', 'Operating'))
        country_mm = st.sidebar.radio("country", ('Acquired', 'Closed', 'Operating'))
        diff_funding_months_mm = st.sidebar.radio("diff_funding_months", ('Acquired', 'Closed', 'Operating'))
        diff_first_funding_months_mm = st.sidebar.radio("diff_first_funding_months", ('Acquired', 'Closed', 'Operating'))
        round_A_H_total_mm = st.sidebar.radio("round_A_H_total", ('Acquired', 'Closed', 'Operating'))
        angel_status_mm = st.sidebar.radio("angel_status", ('Acquired', 'Closed', 'Operating'))
        grant_status_mm = st.sidebar.radio("grant_status", ('Acquired', 'Closed', 'Operating'))
        avg_fund_size_mm = st.sidebar.radio("avg_fund_size", ('Acquired', 'Closed', 'Operating'))
        ratio_seed_tot_mm = st.sidebar.radio("ratio_seed_tot", ('Acquired', 'Closed', 'Operating'))
        ratio_debt_tot_mm = st.sidebar.radio("ratio_debt_tot", ('Acquired', 'Closed', 'Operating'))
        convertible_status_mm = st.sidebar.radio("convertible_status", ('Acquired', 'Closed', 'Operating'))
        seed_quartiles_mm = st.sidebar.radio("seed_quartiles", ('Acquired', 'Closed', 'Operating'))
        angel_degree_mm = st.sidebar.radio("angel_degree", ('Acquired', 'Closed', 'Operating'))
        tot_funding_degree_mm = st.sidebar.radio("tot_funding_degree", ('Acquired', 'Closed', 'Operating'))
        venture_degree_mm = st.sidebar.radio("venture_degree", ('Acquired', 'Closed', 'Operating'))
        start_postion_mm = st.sidebar.radio("start_postion", ('Acquired', 'Closed', 'Operating'))
        secondary_status_mm = st.sidebar.radio("secondary_status", ('Acquired', 'Closed', 'Operating'))
        recency_mm = st.sidebar.radio("recency", ('Acquired', 'Closed', 'Operating'))

        data = {'market': market_mm,
                'funding_total_usd': funding_total_usd_mm,
                'status': status_mm,
                #'seed': seed_mm,
                'venture': venture_mm,
                'equity_crowdfunding': equity_crowdfunding_mm,
                'undisclosed': undisclosed_mm,
                'convertible_note': convertible_note_mm,
                'debt_financing': debt_financing_mm,
                'angel': angel_mm,
                'grant': grant_mm,
                'private_equity': private_equity_mm,
                'post_ipo_equity': post_ipo_equity_mm,
                'post_ipo_debt': post_ipo_debt_mm,
                'secondary_market': secondary_market_mm,
                'product_crowdfunding': product_crowdfunding_mm,
                'round_A': round_A_mm,
                'round_B': round_B_mm,
                'round_C': round_C_mm,
                'round_D': round_D_mm,
                'round_E': round_E_mm,
                'round_F': round_F_mm,
                'round_G': round_G_mm,
                'round_H': round_H_mm,
                'country': country_mm,
                'diff_funding_months': diff_funding_months_mm,
                'diff_first_funding_months': diff_first_funding_months_mm,
                'round_A_H_total': round_A_H_total_mm,
                'angel_status': angel_status_mm,
                'grant_status': grant_status_mm,
                'avg_fund_size': avg_fund_size_mm,
                'ratio_seed_tot': ratio_seed_tot_mm,
                'ratio_debt_tot': ratio_debt_tot_mm,
                'convertible_status': convertible_status_mm,
                'seed_quartiles': seed_quartiles_mm,
                'angel_degree': angel_degree_mm,
                'tot_funding_degree': tot_funding_degree_mm,
                'venture_degree': venture_degree_mm,
                'start_postion': start_postion_mm,
                'secondary_status': secondary_status_mm,
                'recency': recency_mm}

        features = pd.DataFrame(data, index=[0])
        return features

    input_df = user_input_features()

    st.dataframe(input_df)
