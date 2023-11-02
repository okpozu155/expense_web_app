import streamlit as st
import plotly.graph_objects as go
import calendar
from datetime import datetime
from streamlit_option_menu import option_menu



Incomes = ["salary", "blog", "other sources"]
Expenses = ["Rent", "car", "groceries", "utilities", "savings", "Other Expenses"]
currency = "USD"
page_title = "Income and Expense Tracker"
page_icon =  '💰' 
layout = "centered"

# - - - - - - - - - - - - - - - - -  - - 

st.set_page_config(page_title=page_title, page_icon=page_icon, layout=layout)
st.title(page_title + " "+page_icon)

selected = option_menu(
    menu_title=None,
    options=["Data Entry", "Data Visualization"],
    icons=["U+F4C9", "&#xF17A;"],
    orientation='horizontal',
)


# Drop down menu selecting the period 
year = [(datetime.today().year - 3)+a for a in range(20)]

months = list(calendar.month_name[1:])


hide_st_style = """
    <style>
    #MainMenu {visibility: hidden;} 
    header  {visibility: hidden;}
    footer  {visibility: hidden;}
    </style>
"""
st.markdown(hide_st_style, unsafe_allow_html=True)
#   input and save periods
if selected == "Data Entry":
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
        
    # ------------------------------

if selected== "Data Visualization":
    st.header("Data Visualization")
    with st.form("saved periods"):
        period= st.selectbox("Select Period:", ["2022_March"])
        submitted = st.form_submit_button("plot Period")
        if submitted:
            comment = "Some Text"
            incomes = {"Salary":1500, "Blog": 100, 'Other income':50}
            expenses = {"Rent":600, "Utilities":200, "Groceries": 50, "car":100, 
                            "Other savings":10, "savings":10}
                
        # Create metrics

            total_income = sum(incomes.values())
            total_expenses = sum(expenses.values())
            remaining_budget = total_income - total_expenses
            col1, col2, col3 = st.columns(3)
            col1.metric("Total Income", f"{total_income} {currency}")
            col2.metric("Total Expenses", f"{total_expenses} {currency}")
            col3.metric("Remaining Budget", f"{remaining_budget} {currency}")
            st.text(f"comment: {comment}")

            label = list(incomes.keys()) + [total_expenses] + list(expenses.keys())
            source = list(range(len(incomes))) + [len(incomes)] * len (expenses)
            target = [len(incomes)] * len(incomes) + [label.index(expense) for expense in expenses]
            value = list(incomes.values()) + list(expenses.values())

            link = dict(source=source, target=target, value=value)
            node = dict(label=label, pad=20, thickness=30, color='#E694FF')
            data= go.Sankey(link=link, node=node)

            fig = go.Figure(data)
            fig.update_layout(margin=dict(l=0,r=0,t=5,b=5))
            st.plotly_chart(fig, use_container_width=True)
            fig.show()




