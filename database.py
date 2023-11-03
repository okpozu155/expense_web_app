from pymongo import MongoClient
client = MongoClient('localhost', 27017)

db = client['finance_records']

coll = db['income_expense']


# --- DATABASE INTERFACE ---
# def get_all_periods():
#     items = db.fetch_all_periods()
#     periods = [item["key"] for item in items]
#     return coll.insert_one(periods)


# def init_connection():
#     return MongoClient(**st.secrets["mongo"])

# client = init_connection()
db = client['my_db']
coll = db["my_coll"]


period_data = db.my_coll.find_one()

print(period_data)
periods = [item["key"] for item in period_data.items()]
# comment = period_data.get("comment")
# expenses = period_data.get("expenses")
# incomes = period_data.get("incomes")

print(periods)








def get_all_periods():
    items = db.my_coll.find()  # Find all documents in the collection
    periods = [item["_id"] for item in items]  # Assuming "_id" is the period identifier
    return periods

if selected == "Data Visualization":
    st.header("Data Visualization")
    with st.form("saved periods"):
        periods = get_all_periods()
        if not periods:
            st.warning("No saved periods found.")
        else:
            period = st.selectbox("Select Period:", periods)
            submitted = st.form_submit_button("Plot Period")

            if submitted:
                # Get data for the selected period
                period_data = db.my_coll.find_one({"_id": period})

                if period_data:
                    comment = period_data.get("comment")
                    expenses = period_data.get("expenses")
                    incomes = period_data.get("incomes")
                    st.write("Comment:", comment)
                    st.write("Expenses:", expenses)
                    st.write("Incomes:", incomes)
                else:
                    st.warning("Selected period not found in the database.")





                # ... Calculate metrics, create Sankey diagram, etc.

            else:
                st.warning("Selected period not found in the database.")
