import streamlit as st
import pandas as pd
import xgboost as xgb
import numpy as np

# -------------------------------
# LOAD MODEL
# -------------------------------
model = xgb.XGBClassifier()
model.load_model("og_model.json")

st.set_page_config(page_title="Return Optimization System", layout="wide")

# -------------------------------
# HEADER
# -------------------------------
st.title("📦 Reverse Logistics & Return Optimization System")
st.markdown("AI-powered decision intelligence for e-commerce returns")

# -------------------------------
# SIDEBAR INPUT
# -------------------------------
st.sidebar.header("🔧 Input Features")

price = st.sidebar.slider("💰 Product Price", 0, 5000, 500)
freight_ratio = st.sidebar.slider("🚚 Freight Ratio", 0.0, 1.0, 0.2)
delivery_days = st.sidebar.slider("📅 Delivery Days", 1, 20, 5)
delivery_delay = st.sidebar.slider("⏱ Delivery Delay", 0, 10, 0)
review_score = st.sidebar.slider("⭐ Review Score", 1, 5, 4)

customer_return_rate = st.sidebar.slider("👤 Customer Return Rate", 0.0, 1.0, 0.2)
product_return_rate = st.sidebar.slider("📦 Product Return Rate", 0.0, 1.0, 0.2)

sentiment_score = st.sidebar.slider("🧠 Sentiment Score", -1.0, 1.0, 0.0)
keyword_flag = st.sidebar.selectbox("⚠️ Issue Keywords Present?", [0, 1])
risky_customer = st.sidebar.selectbox("🚨 Risky Customer?", [0, 1])

# -------------------------------
# PREDICTION BUTTON
# -------------------------------
if st.sidebar.button("🚀 Predict Return Risk"):

    input_data = np.array([[
        price, freight_ratio, delivery_days, delivery_delay,
        review_score, customer_return_rate, product_return_rate,
        sentiment_score, keyword_flag, risky_customer
    ]])

    prediction = model.predict(input_data)[0]
    prob = model.predict_proba(input_data)[0][1]

    # -------------------------------
    # DECISION ENGINE (NEW 🔥)
    # -------------------------------
    def decision_logic(prob):
        if prob > 0.8:
            return "Auto Refund"
        elif prob > 0.5:
            return "Manual Review"
        else:
            return "No Refund"

    decision = decision_logic(prob)

    # -------------------------------
    # COST MODEL (NEW 🔥)
    # -------------------------------
    def cost_estimation(price, decision):
        if decision == "Auto Refund":
            return price * 1.2
        elif decision == "Manual Review":
            return price * 0.7
        else:
            return price * 0.2

    cost = cost_estimation(price, decision)

    # -------------------------------
    # OUTPUT
    # -------------------------------
    st.subheader("📊 Prediction Result")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Return Probability", f"{prob*100:.2f}%")

    col2.metric("Prediction", "Return" if prediction == 1 else "No Return")

    col3.metric("Decision", decision)

    col4.metric("Estimated Cost", f"${cost:.2f}")

    # -------------------------------
    # RISK LEVEL
    # -------------------------------
    if prob > 0.7:
        st.error("⚠️ High Risk → Immediate Action Required")
    elif prob > 0.4:
        st.warning("⚠️ Medium Risk → Investigate Further")
    else:
        st.success("✅ Low Risk → Safe Order")

    # -------------------------------
    # INSIGHTS (IMPROVED)
    # -------------------------------
    st.subheader("🧠 Key Insights")

    insights = []

    if delivery_delay > 3:
        insights.append("Late delivery significantly increases return probability")

    if review_score <= 2:
        insights.append("Low review score → customer dissatisfaction")

    if sentiment_score < -0.2:
        insights.append("Negative sentiment detected from NLP")

    if customer_return_rate > 0.5:
        insights.append("Customer has high historical return behavior")

    if product_return_rate > 0.5:
        insights.append("Product has high return history")

    if keyword_flag == 1:
        insights.append("Complaint keywords detected (damaged, defective, etc.)")

    if risky_customer == 1:
        insights.append("Customer flagged as risky")

    if insights:
        for i in insights:
            st.warning(f"⚡ {i}")
    else:
        st.success("No major risk factors detected")

    # -------------------------------
    # BUSINESS RECOMMENDATION (NEW 🔥)
    # -------------------------------
    st.subheader("🏢 Business Recommendation")

    if decision == "Auto Refund":
        st.error("💸 Recommend immediate refund to avoid customer churn")
    elif decision == "Manual Review":
        st.warning("🔍 Investigate issue before approving return")
    else:
        st.success("📦 Do not initiate return — low risk order")

    # -------------------------------
    # VISUALIZATION (CONNECTED TO INPUTS 🔥)
    # -------------------------------
    st.subheader("📈 Feature Impact Visualization")

    chart_df = pd.DataFrame({
        "Feature": [
            "Review Score",
            "Delivery Delay",
            "Sentiment",
            "Customer Behavior"
        ],
        "Impact": [
            1 - (review_score / 5),
            delivery_delay / 10,
            abs(sentiment_score),
            customer_return_rate
        ]
    })

    st.bar_chart(chart_df.set_index("Feature"))

# -------------------------------
# FOOTER
# -------------------------------
st.markdown("---")
st.markdown("🚀 Built for industry-level reverse logistics decision making")