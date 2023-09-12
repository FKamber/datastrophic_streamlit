#############################################
# Kullanılacak Kütüphaneler
#############################################


import numpy as np
import pandas as pd
import seaborn as sns
import streamlit as st

from streamlit_extras.let_it_rain import rain
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report
import matplotlib.pyplot as plt



import pickle
import joblib


from streamlit_option_menu import option_menu

#############################################
# Sayfaların Oluşumu
#############################################

st.set_page_config(
    page_title='DataStrophic2',
    layout="wide",
    page_icon="💰")

page_bg_img = """
<style>
[data-testid="stSidebar"] {
background-image: url("https://i.pinimg.com/originals/9f/73/95/9f73957ced55190e40212bf1da84dc92.jpg");
background-size: cover;
}
</style>
"""
st.markdown(page_bg_img,unsafe_allow_html=True)


with st.sidebar:
    selected = option_menu("StartUp Project ", ["Predict", "Analysis", "Report", 'Large Language M', "---", 'Communication'],
                           icons=['house', 'gear', None, "list-task",  "list-task", 'cloud-upload'], menu_icon="cast",
                           default_index=0)


#############################################
# Predict Sayfası
#############################################


if selected == "Predict":
    st.title("StartUp Prediction")
    st.markdown("Girilen Değerler : ")

    # Modeli yükleyin
    # Modelin tam yolunu kullanarak modeli yükleyin

    #with open('x_test.pkl', 'rb') as file:
        #model = pickle.load(file)


    # Kullanıcıdan girdi alacağız
    # Özellikleri belirtin ve değerlerini isteyin

    st.sidebar.title("Startup Değerlerinizi Giriniz")

    # Collects user input features into dataframe
    #uploaded_file = st.sidebar.file_uploader("Upload your input CSV file", type=["csv"])
    #if uploaded_file is not None:
        #input_df = pd.read_csv(uploaded_file)
    def user_input_features():
        country_mm = st.sidebar.selectbox("country", ( 'Turkey', 'United States', 'United Kingdom',
                                                   'Canada', 'China', 'Germany', 'France','India',
                                                   'Israel', 'Spain', 'Russia', 'Sweden', 'Italy', 'Netherlands',
                                                   'Ireland', 'Singapure', 'Norway', 'Poland'))
        recency_mm = st.sidebar.number_input("recency", step=100)
        funding_total_usd_mm = st.sidebar.slider('funding_total_usd', 0, 100000, 1000000000)
        seed_mm = st.sidebar.slider('seed', 0, 100000, 10000000)
        venture_mm = st.sidebar.number_input('venture', step=1)
        round_A_mm = st.sidebar.number_input('round_A', step=1)
        diff_funding_months_mm = st.sidebar.date_input("diff_funding_months")   #burası date aralığı olabilir ?
        diff_first_funding_months_mm = st.sidebar.date_input("diff_first_funding_months" ) # https://docs.streamlit.io/library/api-reference/widgets/st.date_input buradan yapılabilir
        round_A_H_total_mm = st.sidebar.number_input('round_A_H_total', step=1)
        avg_fund_size_mm = st.sidebar.slider("avg_fund_size", 0, 10000, 9009090)

        #market_mm = st.sidebar.selectbox('market', ('Publishing','Electronics','Tourism'
        #                                             'Software','Biotechnology','Education'))
        #status_mm = st.sidebar.radio("Status",('Acquired', 'Closed', 'Operating'))
        #equity_crowdfunding_mm = st.sidebar.radio("equity_crowdfunding",('Acquired', 'Closed', 'Operating'))
        #undisclosed_mm = st.sidebar.radio("undisclosed",('Acquired', 'Closed', 'Operating'))
        #convertible_note_mm = st.sidebar.radio("convertible_note",('Acquired', 'Closed', 'Operating'))
        #debt_financing_mm = st.sidebar.radio("debt_financing",('Acquired', 'Closed', 'Operating'))
        #angel_mm = st.sidebar.radio("angel", ('Acquired', 'Closed', 'Operating'))
        #grant_mm = st.sidebar.radio("grant", ('Acquired', 'Closed', 'Operating'))
        #private_equity_mm = st.sidebar.radio("private_equity", ('Acquired', 'Closed', 'Operating'))
        #post_ipo_equity_mm = st.sidebar.radio("post_ipo_equity", ('Acquired', 'Closed', 'Operating'))
        #post_ipo_debt_mm = st.sidebar.radio("post_ipo_debt", ('Acquired', 'Closed', 'Operating'))
        #secondary_market_mm = st.sidebar.radio("secondary_market", ('Acquired', 'Closed', 'Operating'))
        #product_crowdfunding_mm = st.sidebar.radio("product_crowdfunding", ('Acquired', 'Closed', 'Operating'))
        #round_B_mm = st.sidebar.radio("round_B", ('Acquired', 'Closed', 'Operating'))
        #round_C_mm = st.sidebar.radio("round_C", ('Acquired', 'Closed', 'Operating'))
        #round_D_mm = st.sidebar.radio("round_D", ('Acquired', 'Closed', 'Operating'))
        #round_E_mm = st.sidebar.radio("round_E", ('Acquired', 'Closed', 'Operating'))
        #round_F_mm = st.sidebar.radio("round_F", ('Acquired', 'Closed', 'Operating'))
        #round_G_mm = st.sidebar.radio("round_G", ('Acquired', 'Closed', 'Operating'))
        #round_H_mm = st.sidebar.radio("round_H", ('Acquired', 'Closed', 'Operating'))
        #angel_status_mm = st.sidebar.radio("angel_status", ('Acquired', 'Closed', 'Operating'))
        #grant_status_mm = st.sidebar.radio("grant_status", ('Acquired', 'Closed', 'Operating'))
        #ratio_seed_tot_mm = st.sidebar.radio("ratio_seed_tot", ('Acquired', 'Closed', 'Operating'))
        #ratio_debt_tot_mm = st.sidebar.radio("ratio_debt_tot", ('Acquired', 'Closed', 'Operating'))
        #convertible_status_mm = st.sidebar.radio("convertible_status", ('Acquired', 'Closed', 'Operating'))
        #seed_quartiles_mm = st.sidebar.radio("seed_quartiles", ('Acquired', 'Closed', 'Operating'))
        #angel_degree_mm = st.sidebar.radio("angel_degree", ('Acquired', 'Closed', 'Operating'))
        #tot_funding_degree_mm = st.sidebar.radio("tot_funding_degree", ('Acquired', 'Closed', 'Operating'))
        #venture_degree_mm = st.sidebar.radio("venture_degree", ('Acquired', 'Closed', 'Operating'))
        #start_postion_mm = st.sidebar.radio("start_postion", ('Acquired', 'Closed', 'Operating'))
        #secondary_status_mm = st.sidebar.radio("secondary_status", ('Acquired', 'Closed', 'Operating'))


        data = {#'market': market_mm,
                'funding_total_usd': funding_total_usd_mm,
                #'status': status_mm,
                'seed': seed_mm,
                'venture': venture_mm,
                #'equity_crowdfunding': equity_crowdfunding_mm,
                #'undisclosed': undisclosed_mm,
                #'convertible_note': convertible_note_mm,
                #'debt_financing': debt_financing_mm,
                #'angel': angel_mm,
                #'grant': grant_mm,
                #'private_equity': private_equity_mm,
                #'post_ipo_equity': post_ipo_equity_mm,
                #'post_ipo_debt': post_ipo_debt_mm,
                #'secondary_market': secondary_market_mm,
                #'product_crowdfunding': product_crowdfunding_mm,
                'round_A': round_A_mm,
                #'round_B': round_B_mm,
                #'round_C': round_C_mm,
                #'round_D': round_D_mm,
                #'round_E': round_E_mm,
                #'round_F': round_F_mm,
                #'round_G': round_G_mm,
                #'round_H': round_H_mm,
                'country': country_mm,
                'diff_funding_months': diff_funding_months_mm,
                'diff_first_funding_months': diff_first_funding_months_mm,
                'round_A_H_total': round_A_H_total_mm,
                #'angel_status': angel_status_mm,
                #'grant_status': grant_status_mm,
                'avg_fund_size': avg_fund_size_mm,
                #'ratio_seed_tot': ratio_seed_tot_mm,
                #'ratio_debt_tot': ratio_debt_tot_mm,
                #'convertible_status': convertible_status_mm,
                #'seed_quartiles': seed_quartiles_mm,
                #'angel_degree': angel_degree_mm,
                #'tot_funding_degree': tot_funding_degree_mm,
                #'venture_degree': venture_degree_mm,
                #'start_postion': start_postion_mm,
                #'secondary_status': secondary_status_mm,
                'recency': recency_mm}

        features = pd.DataFrame(data, index=[0])
        return features

    input_df = user_input_features()

    st.dataframe(input_df[['country', 'recency', 'funding_total_usd', 'seed', 'venture',
                           'round_A', 'diff_funding_months', 'diff_first_funding_months',
                           'round_A_H_total', 'avg_fund_size']])

    # verisetini alıyoruz
    #df = pd.read_csv("balanced_df.csv")

    with open('pickle_clean_crunchbase', 'rb') as file:
        df = pickle.load(file)



    tahmin_seti = pd.concat([input_df, df], axis=0)
    st.write("Let's view the merged dataset ...")
    st.write(tahmin_seti[['country', 'recency', 'funding_total_usd', 'seed', 'venture',
                           'round_A', 'diff_funding_months', 'diff_first_funding_months',
                           'round_A_H_total', 'avg_fund_size']].head())



#############################################
# Analiz Sayfası
#############################################

if selected == "Analysis":


    st.write("Bu kısım geliştirilmektedir")

#############################################
# Raporlama Sayfası
#############################################

if selected == "Report":
    #report = pd.read_csv("visualsdf.csv")

    st.write(" Veri Setimizi Tanıyalım")

    st.title("Statistical Reports and Visualizations for the Hitters Dataset")

    with open('pickle_clean_crunchbase.pkl', 'rb') as file:
        report_df = pickle.load(file)

    st.write("### Dataset:")
    st.write(report_df.head())

    show_profile_report = st.checkbox("Show Pandas Profiling Report")

    if show_profile_report:
        st.write("### Pandas Profiling Report:")
        profile = ProfileReport(report_df, title="Pandas Profiling Report", explorative=True)
        st_profile_report(profile)

        # Veri kümesinin özellik dağılımlarını göster
        st.write("### Feature Distributions:")
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.histplot(data=report_df, ax=ax)
        plt.xticks(rotation=45)
        st.pyplot(fig)

        # Sütunlar arasındaki ilişkileri göster
        st.write("### Column Interactions:")
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.pairplot(data=report_df, diag_kind="kde")
        st.pyplot(fig)

        # Korelasyon matrisini göster
        st.write("### Correlation Matrix:")
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.heatmap(report_df.corr(), annot=True, cmap="coolwarm", linewidths=.5, ax=ax)
        st.pyplot(fig)




#############################################
# LLM Sayfası
#############################################

if selected == "Large Language M":

    st.title("Bu Bölüm LLM içindir")



#############################################
# Communication Sayfası
#############################################

if selected == "Communication":
    #st.balloons()

    rain(
        emoji="🎈",
        font_size=54,
        falling_speed=5,
        animation_length="infinite",
    )

    st.markdown('<h1 style="text-align: center;">🤖 DataStrophic Team 🤖</h1>', unsafe_allow_html=True)
    #st.title("🤖 DataStrophic Team 🤖 ")

    col1, col2, = st.columns(2)

    with col1:
        st.image("Feyza.png")
        st.markdown('<h3 style="text-align: left;">Feyza Kamber</h3>', unsafe_allow_html=True)

        link_lIn = "[LinkedIn](https://www.linkedin.com/in/feyza-kamber-a61946a8/)"
        st.markdown(link_lIn, unsafe_allow_html=True)

        link_git = "[Github](https://github.com/FKamber)"
        st.markdown(link_git, unsafe_allow_html=True)

        link_kaggle = "[Kaggle](https://www.kaggle.com/feyzakamber)"
        st.markdown(link_kaggle, unsafe_allow_html=True)

        link_medium = "[Medium](https://medium.com/@kamberfeyza)"
        st.markdown(link_medium, unsafe_allow_html=True)

    with col2:
        st.image("Arda.jpeg")
        st.markdown('<h3 style="text-align: left;">Arda Asut</h3>', unsafe_allow_html=True)

        link_lIn = "[LinkedIn](https://www.linkedin.com/in/arda-asut-109800172/)"
        st.markdown(link_lIn, unsafe_allow_html=True)

        link_git = "[Github](https://github.com/FKamber)"
        st.markdown(link_git, unsafe_allow_html=True)

        link_kaggle = "[Kaggle](https://www.kaggle.com/ardoktor)"
        st.markdown(link_kaggle, unsafe_allow_html=True)

        link_medium = "[Medium](https://medium.com/@kamberfeyza)"
        st.markdown(link_medium, unsafe_allow_html=True)

