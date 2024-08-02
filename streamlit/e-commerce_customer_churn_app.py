# library
import os
import streamlit as st
import pandas as pd
import pickle
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.express as px

# Page config - This must be the first Streamlit command
st.set_page_config(page_title="ShopWise Churn Predictor", layout="wide", initial_sidebar_state="expanded")

# Set dark theme
st.markdown("""
<style>
    .reportview-container {
        background-color: #0E1117;
        color: #FAFAFA;
    }
    .sidebar .sidebar-content {
        background-color: #262730;
    }
    .Widget>label {
        color: #FAFAFA;
    }
    .stTextInput>div>div>input {
        background-color: #262730;
        color: #FAFAFA;
    }
    .stSelectbox>div>div>select {
        background-color: #262730;
        color: #FAFAFA;
    }
    .stSlider>div>div>div>div {
        background-color: #4CAF50;
    }
    .stButton>button {
        color: #0E1117;
        background-color: #4CAF50;
        border-radius: 5px;
    }
</style>
""", unsafe_allow_html=True)

# Model and System
MAIN_PATH = os.path.abspath(os.getcwd())
PATH_MODEL = os.path.join(MAIN_PATH, "final_model.sav")
lgbm = pickle.load(open(PATH_MODEL, 'rb'))

# Sidebar
with st.sidebar:
    st.image("logo_shopwise.png", width=200)
    st.title("Navigation")
    page = st.radio("", ["🏠 Home", "🔮 Predict", "ℹ️ About"])

# Home page
if page == "🏠 Home":
    st.title("Welcome to ShopWise Churn Predictor")
    st.write("""
    Our AI-powered tool helps you identify customers at risk of churning. 
    Let's keep your business thriving! 🚀
    """)
    
    col1, col2 = st.columns(2)
    with col1:
        st.image("e-commerce_churn.png", width=400)
    with col2:
        st.subheader("Why use ShopWise?")
        st.markdown("""
        - 🎯 Precision targeting
        - 💡 Actionable insights
        - 📈 Boost retention rates
        - 💰 Increase customer lifetime value
        """)
    
    st.info("Navigate to the '🔮 Predict' page to start analyzing customer data!")

# Predict page
elif page == "🔮 Predict":
    st.title("Customer Churn Prediction")
    
    col1, col2 = st.columns(2)
    
    with col1:
        tenure = st.slider("📅 Tenure (Months)", 0, 60, 12)
        wh = st.slider("🏠 Warehouse to Home Distance (km)", 1, 50, 10)
        status = st.selectbox("💍 Marital Status", ('Single', 'Married', 'Divorced'))
        address = st.number_input("📍 Number of Addresses", 1, 10, 1)
        category = st.selectbox("🛍️ Preferred Order Category", ('Laptop & Accessory', 'Mobile Phone', 'Fashion', 'Others', 'Grocery'))
    
    with col2:
        device = st.number_input("📱 Number of Devices Registered", 1, 10, 1)
        score = st.slider("⭐ Satisfaction Score", 1, 5, 3)
        last_order = st.number_input("🗓️ Days Since Last Order", 0, 365, 7)
        cashback = st.number_input("💸 Cashback Amount ($)", 0.0, 1000.0, 50.0, 0.01)
        complain = st.selectbox("😟 Has Complained?", ('No', 'Yes'))

    if st.button("🔍 Predict Churn Probability", key="predict"):
        with st.spinner("Analyzing customer data..."):
            # Prepare feature dataframe
            feature = pd.DataFrame({
                'NumberOfDeviceRegistered': [device],
                'SatisfactionScore': [score],
                'NumberOfAddress': [address],
                'Complain': [1 if complain == 'Yes' else 0],
                'Tenure': [tenure],
                'WarehouseToHome': [wh],
                'DaySinceLastOrder': [last_order],
                'CashbackAmount': [cashback],
                'PreferedOrderCat': [category],
                'MaritalStatus': [status]
            })

            # Make prediction
            prob = lgbm.predict_proba(feature)
            churn_prob = prob[0][1]

            # Create subplot with gauge chart and donut chart
            fig = make_subplots(rows=1, cols=2, specs=[[{'type': 'indicator'}, {'type': 'domain'}]])

            # Gauge chart
            fig.add_trace(go.Indicator(
                mode = "gauge+number",
                value = churn_prob,
                title = {'text': "Churn Probability", 'font': {'color': '#FAFAFA'}},
                gauge = {
                    'axis': {'range': [None, 1], 'tickwidth': 1, 'tickcolor': "#FAFAFA"},
                    'bar': {'color': "#4CAF50"},
                    'steps' : [
                        {'range': [0, 0.5], 'color': "#1E5631"},
                        {'range': [0.5, 0.7], 'color': "#FFA500"},
                        {'range': [0.7, 1], 'color': "#8B0000"}],
                    'threshold' : {'line': {'color': "red", 'width': 4}, 'thickness': 0.75, 'value': 0.7}},
                number = {'font': {'color': '#FAFAFA'}}
            ), row=1, col=1)

            # Donut chart
            fig.add_trace(go.Pie(
                labels=['Retention', 'Churn'],
                values=[1-churn_prob, churn_prob],
                hole=.3,
                marker_colors=['#1E5631', '#8B0000'],
                textinfo='label+percent',
                textfont={'color': '#FAFAFA'}
            ), row=1, col=2)

            fig.update_layout(height=500, width=1000, paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
            st.plotly_chart(fig)

            if churn_prob > 0.7:
                st.error("🚨 High risk of churn! Implement retention strategies ASAP.")
            elif churn_prob > 0.5:
                st.warning("⚠️ Moderate risk of churn. Monitor closely and engage proactively.")
            else:
                st.success("✅ Low risk of churn. Keep up the good work!")

# About page
elif page == "ℹ️ About":
    st.title("About ShopWise Churn Predictor")
    st.write("""
    ShopWise Churn Predictor uses cutting-edge machine learning to analyze customer behavior 
    and identify potential churners. Our model helps you retain valuable customers and grow your business.
    """)
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Key Features")
        st.markdown("""
        - 🧠 Advanced ML algorithms
        - 📊 Real-time predictions
        - 🎯 Actionable insights
        - 🔄 Continuous learning
        """)
    with col2:
        st.subheader("")
        st.image("e-commerce_churn.png", width=300)
    
    st.subheader("Get in Touch")
    st.markdown("""
    Have questions or need support? Reach out to me:
    - 📧 Email: samuelsemaya29@gmail.com
    - 🌐 Website: https://www.linkedin.com/in/samuelsemaya/
    """)

# Footer
st.markdown("---")
st.markdown("© 2024 ShopWise Churn Predictor. All rights reserved.")

# Add a fun fact or tip in the sidebar
with st.sidebar:
    st.markdown("---")
    st.subheader("💡 Did You Know?")
    facts = [
        "Acquiring a new customer can cost 5 times more than retaining an existing one.",
        "A 5% increase in customer retention can increase profits by 25-95%.",
        "The success rate of selling to an existing customer is 60-70%, compared to 5-20% for a new customer."
    ]
    st.info(facts[int(pd.Timestamp.now().timestamp()) % len(facts)])