import requests
from datetime import datetime
import streamlit as st
import pandas as pd

API_URL = "http://127.0.0.1:8000"

def analytics_by_month_tab():

    # col1, col2 = st.columns(2)
    # with col1:
    #     start_date = st.date_input("Start Date", datetime(2024, 8, 1))
    #
    # with col2:
    #     end_date = st.date_input("End Date", datetime(2024, 8, 5))

    if st.button("Get Analytics By Month"):
        # payload = {
        #     "start_date": start_date.strftime("%Y-%m-%d"),
        #     "end_date": end_date.strftime("%Y-%m-%d")
        # }
        response = requests.get(f"{API_URL}/analytics/months/")

        if response.status_code == 200:
            response = response.json()

            # data = {
            #     "Month":list(response.keys()),
            #     "Total":[response[category]["total"] for category in response.keys()],
            #     "Percentage":[response[category]["percentage"] for category in response.keys()]
            # }

            # {
            #     "year": 2024,
            #     "month_number": 9,
            #     "month_name": "September",
            #     "average_transaction": 184.23,
            #     "total_transactions": 26
            # },
            # {
            #     "year": 2026,
            #     "month_number": 8,
            #     "month_name": "August",
            #     "average_transaction": 110.0,
            #     "total_transactions": 2
            # }
            data = {
                "Month": [f"{row['year']} {row['month_name']}" for row in response],
                "Average Transactions":[row['average_transaction'] for row in response],
                "Total Transactions":[row['total_transactions'] for row in response]
            }

            df = pd.DataFrame(data)
            # df_sorted = df.sort_values(by=['Percentage'], ascending=False)
            #

            st.header("Expense Breakdown By Month")
            st.bar_chart(df.set_index("Month")["Average Transactions"], x_label="Months",
                         y_label="Average Transactions", use_container_width=True)
            st.table(df)
            # st.bar_chart(data=df_sorted.set_index('Category')["Percentage"], height= 500, use_container_width=True)
            # st.table(df_sorted)