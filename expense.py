import streamlit as st

def main():
    st.title("Expense Manager")

    # Display choice options
    st.subheader("Choose a Purpose:")
    choice = st.radio("Select your choice", ("NORMAL PURPOSE", "HEALTH PURPOSE"))

    # Process based on choice
    if choice == "NORMAL PURPOSE":
        st.subheader("Normal Purpose Management")

        # Input values for main and primary accounts
        mainaccount = st.number_input("Enter the amount in main account:", min_value=0.0, step=0.01)
        primaryaccount = st.number_input("Fixed amount in the primary account:", min_value=0.0, step=0.01)

        if primaryaccount < mainaccount:
            # Input value for secondary account
            secondaryaccount = st.number_input("Amount in the secondary account:", min_value=0.0, step=0.01)

            if secondaryaccount < mainaccount - primaryaccount:
                # Input limit to be used in one month
                z = st.number_input("The limit of the account to be used in 1 month:", min_value=0.0, step=0.01)

                if z < primaryaccount:
                    # Input amount used in the first month
                    amount = st.number_input("Enter amount used in 1st month:", min_value=0.0, step=0.01)

                    # Display results based on conditions
                    if st.button("Submit"):
                        if amount < 0.8 * z:
                            st.success("Payment will be done without fail")
                        elif 0.8 * z <= amount < z:
                            st.warning("Warning but payment will happen")
                        elif z <= amount < z + secondaryaccount:
                            st.info("Now, switch to emergency account")
                        elif amount > z + secondaryaccount:
                            st.error("Payment unsuccessful")
                else:
                    st.error("Invalid input for the monthly limit (z).")
            else:
                st.error("Invalid input for the secondary account.")
        else:
            st.error("Error in input for the primary account.")

    elif choice == "HEALTH PURPOSE":
        st.subheader("Health Purpose Management")

        # Input values for main account and health purpose
        mainaccount = st.number_input("Enter amount in main account:", min_value=0.0, step=0.01)
        healthaccount = st.number_input("Enter amount required for health purpose:", min_value=0.0, step=0.01)

        # Display results based on conditions
        if st.button("Submit"):
            if healthaccount <= mainaccount:
                st.success("Payment directly by bank.")  # Only valid UPI ID will be scanned
            else:
                st.error("Error: Insufficient funds in the main account.")

if __name__ == "__main__":
    main()
