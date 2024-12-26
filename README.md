Expense Manager
A simple web application built using Streamlit for managing expenses related to normal purposes and health purposes. The app allows users to input amounts in various accounts and offers guidance on how payments can be processed depending on the conditions defined.

Features
Normal Purpose Management

Users can input the amount in the main account and a fixed amount in the primary account.
Based on the balance in the primary and secondary accounts, users can set a limit for monthly usage.
Provides feedback about payment processing, with options for different scenarios:
Payment will be processed without fail.
Payment will happen with a warning.
Emergency account switch recommended.
Payment unsuccessful due to insufficient funds.
Health Purpose Management

Users can input the amount in the main account and the amount required for health purposes.
If sufficient funds are available in the main account, payment will be processed directly.
If insufficient funds, an error is displayed indicating insufficient funds for the health purpose.
Prerequisites
To run this application, ensure you have the following installed:

Python 3.x
Streamlit library
To install Streamlit, run:
bash
Copy code
pip install streamlit
Running the Application
Clone this repository or download the Python file app.py.
Open a terminal and navigate to the folder where the file is saved.
Run the following command to start the Streamlit app:
bash
Copy code
streamlit run app.py
The app will open in your default web browser.
Usage
Normal Purpose Management
Enter the amount in the main account: This is the total available balance in your main account.
Enter the fixed amount in the primary account: This is the amount that is reserved or fixed for primary use.
If the primary account amount is less than the main account balance:
Enter the amount in the secondary account: This is the emergency or secondary balance.
Enter the limit for usage in one month: The maximum amount that can be used in a month from the primary account.
Enter the amount used in the first month: Based on this input, the system will provide feedback on whether the payment will be successful or if an emergency account needs to be used.
Health Purpose Management
Enter the amount in the main account: This is the total balance in the main account.
Enter the amount required for health purposes: This is the amount needed for health-related expenses.
If the main account has sufficient funds, a success message will be shown. Otherwise, an error message will indicate insufficient funds.
Example Scenarios
Normal Purpose:
If the monthly limit is set to $100, and you used only $70, the app will confirm that the payment will proceed without issues.
If you try to use more than the total available amount (primary account + secondary account), the payment will fail.
Health Purpose:
If the required health amount is less than or equal to the main account balance, the app will confirm the payment can be processed.
If the health amount exceeds the main account balance, an error message will be shown indicating insufficient funds.
Dependencies
The following libraries are required:

streamlit
You can install the dependencies using the following command:

bash
Copy code
pip install -r requirements.txt
License
This project is licensed under the MIT License - see the LICENSE file for details.

This README provides an overview of how to set up, run, and use the Expense Manager application. Let me know if you'd like to make any adjustments!



