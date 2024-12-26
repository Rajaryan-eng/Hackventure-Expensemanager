import streamlit as st
import pandas as pd
import datetime
import matplotlib.pyplot as plt
from PIL import Image

def main():
    # Set page configuration
    st.set_page_config(page_title="Expense Manager", page_icon="💰", layout="wide")

    # Link to local PNG image file
    image_path = "C:/Users/Dell/Downloads/image_hack.png"  # Local file path
    background_image = f'url("file://{image_path}")'

    # Apply custom CSS to set the background image with reduced height
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: {background_image};
            background-size: 100% auto;  /* Reduces height while maintaining aspect ratio */
            background-position: center;  /* Centers the image */
            background-attachment: fixed;  /* Keeps the background fixed during scrolling */
            min-height: 100vh;  /* Ensures the background image covers the full height of the viewport */
        }}
        </style>
        """, unsafe_allow_html=True
    )

    # Add a banner image or title
    st.image(image_path, use_column_width=True)

    # Title and description
    st.markdown("<h1 style='text-align: center; color: #4CAF50;'>Expense Manager</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #555;'>Manage your expenses efficiently with our simple and intuitive app.</p>", unsafe_allow_html=True)

    # Add a separator line
    st.markdown("---")

    # Initialize session state to store expenses
    if "expenses" not in st.session_state:
        st.session_state["expenses"] = []

    # Input form for adding expenses
    with st.form("expense_form"):
        date = st.date_input("Date", value=datetime.date.today())
        category = st.selectbox("Category", ["Food", "Transportation", "Rent", "Entertainment", "Other"])
        description = st.text_input("Description")
        amount = st.number_input("Amount", min_value=0.0, format="%.2f")
        submitted = st.form_submit_button("Add Expense")

        if submitted:
            if description and amount > 0:
                st.session_state["expenses"].append({
                    "Date": date,
                    "Category": category,
                    "Description": description,
                    "Amount": amount,
                })
                st.success("Expense added successfully!")
            else:
                st.error("Please provide valid input.")

    # Display expenses as a table
    st.subheader("Expense Table")
    if st.session_state["expenses"]:
        df = pd.DataFrame(st.session_state["expenses"])
        st.dataframe(df)

        # Show summary
        st.subheader("Summary by Category")
        category_summary = df.groupby("Category")["Amount"].sum().reset_index()
        st.dataframe(category_summary)

        # Bar chart for visualization
        st.subheader("Spending by Category")
        fig, ax = plt.subplots(figsize=(12, 6))  # Adjust width and height (wider graph)
        ax.bar(category_summary["Category"], category_summary["Amount"], color="green")  # Changed color to green
        ax.set_xlabel("Category")
        ax.set_ylabel("Amount")
        ax.set_title("Spending by Category")
        st.pyplot(fig)
    else:
        st.info("No expenses added yet.")

    # Option to reset expenses
    if st.button("Reset Expenses"):
        st.session_state["expenses"] = []
        st.success("Expenses have been reset.")

    # Add a separator line
    st.markdown("---")

    # Display choice options with cards
    st.subheader("Choose a Purpose:")
    choice = st.radio(
        "",
        ("NORMAL PURPOSE", "HEALTH PURPOSE"),
        index=0,
        horizontal=True,
        label_visibility="collapsed",
        help="Select the type of expense management you want."
    )

    st.markdown("---")

    # Process based on choice
    if choice == "NORMAL PURPOSE":
        st.markdown("<h3 style='color: #4CAF50;'>Normal Purpose Management</h3>", unsafe_allow_html=True)

        # Input values for main account
        col1, col2 = st.columns([1, 1])  # Ensure equal width for both columns
        with col1:
            mainaccount = st.number_input("💼 Main Account Balance:", min_value=0.0, step=0.01, help="Enter the total amount in your main account.")
        with col2:
            secondaryaccount = st.number_input("🛡️ Secondary Account Balance:", min_value=0.0, step=0.01, help="Enter the amount in your secondary account.")

        if secondaryaccount < mainaccount:
            # Input limit to be used in one month
            z = st.number_input("📅 Monthly Expense Limit:", min_value=0.0, step=0.01, help="Enter the monthly spending limit.")

            if z < mainaccount:
                # Automatically calculate the sum of expenses for the current month
                if st.session_state["expenses"]:
                    df = pd.DataFrame(st.session_state["expenses"])
                    current_month = datetime.date.today().month
                    amount = df[df["Date"].apply(lambda x: x.month == current_month)]["Amount"].sum()
                else:
                    amount = 0.0

                # Display results based on conditions
                if st.button("Submit", key="normal_submit"):
                    st.write(f"📊 Amount Used in 1st Month: {amount:.2f}")
                    if amount < 0.8 * z:
                        st.success("✅ Payment will be done without fail.")
                    elif 0.8 * z <= amount < z:
                        st.warning("⚠️ Warning: Payment will happen, but be cautious!")
                    elif z <= amount < z + secondaryaccount:
                        st.info("🔄 Switch to emergency account for payment.")
                    elif amount > z + secondaryaccount:
                        st.error("❌ Payment unsuccessful.")
            else:
                st.error("❌ Invalid input for the monthly limit (z).")
        else:
            st.error("❌ Invalid input for the secondary account.")

    elif choice == "HEALTH PURPOSE":
        st.markdown("<h3 style='color: #FF5722;'>Health Purpose Management</h3>", unsafe_allow_html=True)

        # Input values for main account and health purpose
        col1, col2 = st.columns([1, 1])  # Ensure equal width for both columns
        with col1:
            mainaccount = st.number_input("💼 Main Account Balance:", min_value=0.0, step=0.01, help="Enter the total amount in your main account.")
        with col2:
            healthaccount = st.number_input("🏥 Health Expense Amount:", min_value=0.0, step=0.01, help="Enter the amount required for health purposes.")

        # Display results based on conditions
        if st.button("Submit", key="health_submit"):
            if healthaccount <= mainaccount:
                st.success("✅ Payment directly by bank. (Ensure UPI ID is valid)")
            else:
                st.error("❌ Error: Insufficient funds in the main account.")

    # Add footer
    st.markdown("---")
    st.markdown(
        "<p style='text-align: center; color: #999;'>Made with ❤️ during a Hackathon</p>",
        unsafe_allow_html=True,
    )

if __name__ == "__main__":
    main()
