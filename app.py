# Importing pakages
import streamlit as st
import mysql.connector

from create import create_consumer
from database import create_table_consumer
from delete import delete_consumer
from read import read_consumer
from update import update_consumer
from create import create_cylinder
from database import create_table_cylinder
from delete import delete_cylinder
from read import read_cylinder
from update import update_cylinder
from create import create_orders
from database import create_table_orders
from delete import delete_orders
from read import read_orders
from update import update_orders
from create import create_payment
from database import create_table_payment
from delete import delete_payment
from read import read_payment
from update import update_payment
from create import create_delivery
from database import create_table_delivery
from delete import delete_delivery
from read import read_delivery
from update import update_delivery




def main():
    st.title("Gas agency management")
    tables = ["Consumer", "Cylinder", "Orders", "Payment","Delivery"]
    choice = st.sidebar.selectbox("Tables", tables)
    if choice =="Consumer":
        st.title("Consumer")
        actions = ["Add", "View", "Update", "Delete"]
        choice1 = st.sidebar.selectbox("Actions", actions)

        create_table_consumer()
        if choice1 == "Add":
            st.subheader("Enter Consumer Details:")
            create_consumer()

        elif choice1 == "View":
            st.subheader("View consumer tasks")
            read_consumer()

        elif choice1 == "Update":
            st.subheader("Update consumer tasks")
            update_consumer()

        elif choice1 == "Delete":
            st.subheader("Delete consumer tasks")
            delete_consumer()

        else:
            st.subheader("About tasks")

    if choice =="Cylinder":
        st.title("Cylinder")
        actions = ["Add", "View", "Update", "Delete"]
        choice1 = st.sidebar.selectbox("Actions", actions)

        create_table_cylinder()
        if choice1 == "Add":
            st.subheader("Enter Cylinder Details:")
            create_cylinder()

        elif choice1 == "View":
            st.subheader("View Cylinders tasks")
            read_cylinder()

        elif choice1 == "Update":
            st.subheader("Update Cylinder tasks")
            update_cylinder()

        elif choice1 == "Delete":
            st.subheader("Delete Cylinder tasks")
            delete_cylinder()

        else:
            st.subheader("About tasks")
    

    if choice =="Orders":
        st.title("Orders")
        actions = ["Add", "View", "Update", "Delete"]
        choice1 = st.sidebar.selectbox("Actions", actions)

        create_table_orders()
        if choice1 == "Add":
            st.subheader("Enter Orders Details:")
            create_orders()

        elif choice1 == "View":
            st.subheader("View Orders tasks")
            read_orders()

        elif choice1 == "Update":
            st.subheader("Update Orders tasks")
            update_orders()

        elif choice1 == "Delete":
            st.subheader("Delete Orders tasks")
            delete_orders()

        else:
            st.subheader("About tasks")

    if choice =="Payment":
        st.title("Payment")
        actions = ["Add", "View", "Update", "Delete"]
        choice1 = st.sidebar.selectbox("Actions", actions)

        create_table_payment()
        if choice1 == "Add":
            st.subheader("Enter Payment Details:")
            create_payment()

        elif choice1 == "View":
            st.subheader("View Payment tasks")
            read_payment()

        elif choice1 == "Update":
            st.subheader("Update Payment tasks")
            update_payment()

        elif choice1 == "Delete":
            st.subheader("Delete Payment tasks")
            delete_payment()

        else:
            st.subheader("About tasks")

    if choice =="Delivery":
        st.title("Delivery")
        actions = ["Add", "View", "Update", "Delete"]
        choice1 = st.sidebar.selectbox("Actions", actions)

        create_table_delivery()
        if choice1 == "Add":
            st.subheader("Enter Delivery Details:")
            create_delivery()

        elif choice1 == "View":
            st.subheader("View Delivery tasks")
            read_delivery()

        elif choice1 == "Update":
            st.subheader("Update Delivery tasks")
            update_delivery()

        elif choice1 == "Delete":
            st.subheader("Delete Delivery tasks")
            delete_delivery()

        else:
            st.subheader("About tasks")


if __name__ == '__main__':
    main()
