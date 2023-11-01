import streamlit as st
import plotly.graph_objects as go
import calendar
from datetime import datetime



Incomes = ["salary", "blog", "other sources"]
Expenses = ["Rent", "car", "groceries", "utilities", "savings", "Other Expenses"]
currency = "USD"
page_title = "Income and Expense Tracker"
page_icon =  '💰' 
layout = "centered"

# - - - - - - - - - - - - - - - - -  - - 

st.set_page_config(page_title=page_title, page_icon=page_icon, layout=layout)
st.title(page_title + " "+page_icon)


# Drop down menu selecting the period 
year = [(datetime.today().year - 3)+a for a in range(20)]

months = list(calendar.month_name[1:])


#   input and save periods

st.header(f"Data entry in {currency}")
with st.form("entry form", clear_on_submit=True):
    col1, col2 = st.columns(2)
    col1 = st.selectbox("Select Month", months, key="month")
    col2 = st.selectbox('Select Year', year, key="year")

# ---------

    with st.expander('Income'):
        for income in Incomes:
            st.number_input(f"{income}", format="%i", step=10, min_value=0, key=income)
    with st.expander('Expenses'):
        for expense in Expenses:
            st.number_input(f"{expense}", format="%i", step=10, min_value=0, key=expense)
    with st.expander("Comment"):
        st.text_area("", placeholder= "Enter a comment here . . .", )


    submitted = st.form_submit_button("Save Data")
    if submitted:  
        period = str(st.session_state["year"]) + "_"+ str(st.session_state["month"])
        incomes = {income:st.session_state[income] for income in Incomes}
        expenses = {expense:st.session_state[expense] for expense in Expenses}
        st.write(f"incomes:{incomes}")
        st.write(f"expense:{expenses}")
        st.success("Data Saved")
    


