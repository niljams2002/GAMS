import streamlit as st
from database import add_data_consumer,add_data_cylinder,add_data_orders,add_data_payment,add_data_delivery


def create_consumer():
    col1, col2,col3,col4= st.columns(4)
    with col1:
        user_id = st.text_input("User Id:")
        phone_no = st.text_input("Phone no:")
    with col2:
        firstname = st.text_input("First Name:")
        dob = st.text_input("Date of birth :")
    with col3:
        lastname = st.text_input("Last Name:")
        age = st.text_input("Age")
    with col4:
        street_address = st.text_input("Street address:")
        state = st.text_input("State")

    if st.button("Add Consumer"):
        add_data_consumer(user_id,firstname,lastname,dob,age,street_address,state,phone_no)
        st.success("Successfully added Consumer: {}".format(user_id))



def create_cylinder():
    col1, col2,col3= st.columns(3)
    with col1:
        c_id = st.text_input("Cylinder Id:")
    with col2:
        brand = st.text_input("Brand:")
    
    with col3:
        rate = st.text_input("Rate:")
        

    if st.button("Add Cylinder"):
        add_data_cylinder(c_id,brand,rate)
        st.success("Successfully added Cylinder: {}".format(c_id))

def create_orders():
    col1, col2,col3= st.columns(3)
    with col1:
        user_id = st.text_input("User Id:")
        c_id = st.text_input("Cylinder Id:")
    with col2:
        inv_no = st.text_input("Invoice number:")
        date_of_order = st.text_input("Date of order :")
    with col3:
        quantity = st.text_input("Quantity:")
        amount = st.text_input("Amount :")


    if st.button("Add Order"):
        add_data_orders(user_id,c_id,inv_no,date_of_order,quantity,amount)
        st.success("Successfully added Order: {}".format(inv_no))

def create_payment():
    col1, col2,col3,col4= st.columns(4)
    with col1:
        inv_no = st.text_input("Invoice No:")
       
    with col2:
        transaction_id = st.text_input("Transaction Id:")
   
    with col3:
        status = st.text_input("Payment Status:")
  
    with col4:
        date_of_payment = st.text_input("Date of payment:")


    if st.button("Add payment"):
        add_data_payment(inv_no,transaction_id,status,date_of_payment)
        st.success("Successfully added payment: {}".format(transaction_id))

def create_delivery():
    col1, col2,col3,col4,col5= st.columns(5)
    with col1:
        d_id = st.text_input("Delivery id:")
       
    with col2:
        transaction_id = st.text_input("Transaction Id:")
   
    with col3:
        del_staff = st.text_input("Delivery staff name:")
  
    with col4:
        phone_no = st.text_input("Phone number:")

    with col5:
        date_of_delivery = st.text_input("Date of delivery:")


    if st.button("Add delivery"):
        add_data_delivery(d_id,transaction_id,del_staff,phone_no,date_of_delivery)
        st.success("Successfully added Delivery: {}".format(d_id))