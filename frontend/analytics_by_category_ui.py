import requests
from datetime import datetime
import streamlit as st
import pandas as pd

API_URL = "http://127.0.0.1:8000"

def analytics_by_category_tab():

    col1, col2 = st.columns(2)
    with col1:
        start_date = st.date_input("Start Date", datetime(2024, 8, 1))

    with col2:
        end_date = st.date_input("End Date", datetime(2024, 8, 5))

    if st.button("Get Analytics"):
        payload = {
            "start_date": start_date.strftime("%Y-%m-%d"),
            "end_date": end_date.strftime("%Y-%m-%d")
        }
        response = requests.post(f"{API_URL}/analytics/category/", json=payload)

        if response.status_code == 200:
            response = response.json()

            data = {
                "Category":list(response.keys()),
                "Total":[response[category]["total"] for category in response.keys()],
                "Percentage":[response[category]["percentage"] for category in response.keys()]
            }

            df = pd.DataFrame(data)
            df_sorted = df.sort_values(by=['Percentage'], ascending=False)


            st.header("Expense Breakdown By Category")
            st.bar_chart(data=df_sorted.set_index('Category')["Percentage"], height= 500, use_container_width=True)
            st.table(df_sorted)
