
💰 Income and Expense Tracker

A Streamlit-based application to track incomes and expenses effectively.
Features

    Data Entry: Record incomes and expenses categorized into predefined groups and add comments for specific periods.
    Data Visualization: View incomes, expenses, and remaining budget for specific periods with interactive Sankey diagrams.
    Database Support: Utilizes MongoDB for storing and retrieving data.
    Responsive Design: Simple, clean UI powered by Streamlit.

Prerequisites

    Python 3.7+
    Libraries:
        streamlit
        pymongo
        plotly
        streamlit-option-menu
    MongoDB: A running MongoDB instance (local or cloud-based) with connection details stored in Streamlit's secrets file.

Installation

    Clone the repository:

    git clone https://github.com/your-username/income-expense-tracker.git
    cd income-expense-tracker

    Install dependencies:

    pip install -r requirements.txt

    Set up Streamlit secrets:

    Create a file named secrets.toml in the .streamlit folder:

    [mongo]
    host = "<your_mongo_host>"
    username = "<your_username>"
    password = "<your_password>"
    port = <your_port>

    Run the application:

    streamlit run app.py

Usage
Data Entry

    Navigate to the Data Entry tab.
    Select the month and year for your entry.
    Enter income and expense details in the respective categories.
    Add an optional comment for the period.
    Click Save Data to store the entry in the database.

Data Visualization

    Navigate to the Data Visualization tab.
    Select the desired month and year.
    View:
        Total Income, Expenses, and Remaining Budget.
        Comments for the selected period (if any).
        An interactive Sankey diagram illustrating cash flow.

File Structure
<pre> 
income-expense-tracker/
├── app.py              # Main application script
├── requirements.txt    # List of dependencies
├── README.md           # Project documentation
└── .streamlit/         # Configuration folder for Streamlit
    └── secrets.toml    # MongoDB connection details
</pre>
Visual Examples
Data Entry
Data Entry Screenshot
Data Visualization
Data Visualization Screenshot
Future Enhancements

    Add user authentication for personalized data storage.
    Support for additional currencies.
    Generate downloadable reports in PDF or Excel formats.
    Add recurring income/expense tracking.

