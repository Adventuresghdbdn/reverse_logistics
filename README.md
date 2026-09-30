<div align="center">

# 📦 Reverse Logistics & Return Prediction System

**AI-powered decision intelligence for e-commerce returns**

[![Live App](https://img.shields.io/badge/🚀_Live_Demo-Streamlit-FF4B4B?logo=streamlit&logoColor=white)](https://reverselogistics-llefqsegjziwe5wdetbvng.streamlit.app/)
![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-F7931E?logo=scikitlearn&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?logo=pandas&logoColor=white)
![NLP](https://img.shields.io/badge/NLP-TF--IDF_%2B_Sentiment-4B8BBE)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?logo=streamlit&logoColor=white)

### 👉 [Try the live app](https://reverselogistics-llefqsegjziwe5wdetbvng.streamlit.app/)

</div>

---

## 📌 Overview

Product returns are expensive for e-commerce businesses: shipping costs, handling, and lost inventory all add up. This project predicts **whether an order is likely to be returned** *before* it becomes a problem, so a business can decide how to handle it early.

It is an end-to-end machine learning pipeline, from raw data to a deployed web app, that combines **order and delivery data** with **NLP features from customer reviews**.

## 🎯 Key Highlights

- 🔧 Built an end-to-end **ML pipeline** for return prediction: data cleaning, **feature engineering**, preprocessing, training, tuning, and evaluation, reaching **95%+ accuracy**.
- 🧠 Extracted features from customer reviews using **NLP** (sentiment, TF-IDF) to improve explainability.
- 📊 Evaluated models with **precision, recall, and ROC-AUC**, iterating on features to cut false positives.
- 🚀 Deployed a **Streamlit** app with real-time inference and probability scores; documented the workflow.

---

## 🖥️ Live Demo

🔗 **https://reverselogistics-llefqsegjziwe5wdetbvng.streamlit.app/**

Adjust the order details in the sidebar and click **Predict Return Risk** to get an instant result.

### Prediction, insights and recommendation

<p align="center">
  <img src="images/app_prediction.png" alt="Streamlit app showing return probability, prediction, decision, estimated cost and business recommendation" width="850"/>
</p>

For each order, the app shows:

| Output | Meaning |
|---|---|
| **Return Probability** | Model-estimated chance the order is returned |
| **Prediction** | Return / No Return |
| **Decision** | Suggested refund action |
| **Estimated Cost** | Estimated cost associated with the order |
| **Key Insights** | Risk factors detected for that order |
| **Business Recommendation** | Plain-language action for the operations team |

### Feature impact visualization

<p align="center">
  <img src="images/app_feature_impact.png" alt="Feature impact bar chart showing customer behavior, delivery delay, review score and sentiment" width="850"/>
</p>

A feature impact chart groups the drivers behind a prediction into **Customer Behavior**, **Delivery Delay**, **Review Score** and **Sentiment**, so the result is easier to explain and not just a black-box number.

---

## 🧩 Input Features

The sidebar takes the following inputs:

| Feature | Type |
|---|---|
| 💰 Product Price | Order |
| 🚚 Freight Ratio | Order |
| 📅 Delivery Days | Delivery |
| ⏱️ Delivery Delay | Delivery |
| ⭐ Review Score | Review |
| 👤 Customer Return Rate | Customer history |
| 📦 Product Return Rate | Product history |
| 🧠 Sentiment Score | NLP (from review text) |
| ⚠️ Issue Keywords Present? | NLP (0 / 1) |
| 🚨 Risky Customer? | Flag (0 / 1) |

---

## 🔄 Workflow

```text
Raw data ─► Cleaning ─► Feature engineering ─► NLP features (sentiment, TF-IDF)
        ─► Preprocessing ─► Training & tuning ─► Evaluation ─► Streamlit deployment
```

1. **Data cleaning** of order, delivery and review data.
2. **Feature engineering** of delivery, pricing and return-history signals.
3. **NLP on customer reviews**: sentiment scoring and TF-IDF to capture complaint language and make predictions easier to explain.
4. **Model training and tuning** with Scikit-learn.
5. **Evaluation** using precision, recall and ROC-AUC, not accuracy alone. Features were refined to reduce false positives, which matter because wrongly flagging good orders has a business cost.
6. **Deployment** as a Streamlit app with real-time probability scores.

---

## 🛠️ Tech Stack

`Python` · `Scikit-learn` · `Pandas` · `NLP (TF-IDF, sentiment)` · `Streamlit`

---

## 🚀 Run Locally

```bash
# 1. Clone the repository
git clone https://github.com/Adventuresghdbdn/reverse_logistics.git
cd reverse_logistics

# 2. Install dependencies
pip install -r requirements.txt

# 3. Launch the app
streamlit run app.py
```

> If your main file or requirements file is named differently, adjust the commands above.

---

## 🔮 Future Work

- Add SHAP-based per-order explanations.
- Connect the app to live order data instead of manual inputs.
- Add cost-sensitive thresholds so the refund decision reflects business cost.

---

<div align="center">

Built for industry-level reverse logistics decision making 🚀

⭐ If you found this useful, consider starring the repo!

</div>
