import datetime
import pandas as pd
import streamlit as st
from database import get_details_consumer, view_only_user_ids, view_all_data_consumer, edit_details_consumer,get_details_cylinder, view_only_c_ids, view_all_data_cylinder, edit_details_cylinder,get_details_orders,view_all_data_orders,view_only_inv_no,edit_details_orders
from database import get_details_payment,edit_details_payment,view_all_data_payment,view_only_transaction_ids,get_details_delivery,edit_details_delivery,view_all_data_delivery,view_only_d_ids

def update_consumer():
    result = view_all_data_consumer()
    # st.write(result)
    df = pd.DataFrame(result, columns=['user_id' ,' firstname' , 'lastname' , 'dob' , 'age' , 'street_address' , 'state' , 'phone_no'])
    with st.expander("Current Consumer"):
        st.dataframe(df)
    list_of_dealers = [i[0] for i in view_only_user_ids()]
    selected_dealer = st.selectbox("Consumer to Edit", list_of_dealers)
    selected_result = get_details_consumer(selected_dealer)
    # st.write(selected_result)
    if selected_result:
        user_id= selected_result[0][0]
        firstname=selected_result[0][1]
        lastname= selected_result[0][2]
        dob= selected_result[0][3]
        age=selected_result[0][4]
        street_address=selected_result[0][5]
        state=selected_result[0][6]
        phone_no= selected_result[0][7]

        # Layout of Create
    col1, col2,col3,col4= st.columns(4)
    with col1:
        new_user_id = st.text_input("User Id:",user_id)
        new_phone_no = st.text_input("Phone no:",phone_no)
    with col2:
        new_firstname = st.text_input("First Name:",firstname)
        new_dob = st.text_input("Date of birth :",dob)
    with col3:
        new_lastname = st.text_input("Last Name:",lastname)
        new_age = st.text_input("Age",age)
    with col4:
        new_street_address = st.text_input("Street address:",street_address)
        new_state = st.text_input("State",state)

    if st.button("Update Consumer"):
        edit_details_consumer(new_user_id,new_firstname,new_lastname,new_dob,new_age,new_street_address,new_state,new_phone_no,user_id,firstname,lastname,dob,age,street_address,state,phone_no)
        st.success("Successfully updated:: {} to ::{}".format(user_id, new_user_id))
    result2 = view_all_data_consumer()
    df2 = pd.DataFrame(result2, columns=['user_id' ,' firstname' , 'lastname' , 'dob' , 'age' , 'street_address' , 'state' , 'phone_no'])
    with st.expander("Updated data"):
        st.dataframe(df2)

def update_cylinder():
    result = view_all_data_cylinder()
    # st.write(result)
    df = pd.DataFrame(result, columns=['c_id' ,'brand' , 'rate'])
    with st.expander("Current cylinder"):
        st.dataframe(df)
    list_of_dealers = [i[0] for i in view_only_c_ids()]
    selected_dealer = st.selectbox("cylinder to Edit", list_of_dealers)
    selected_result = get_details_cylinder(selected_dealer)
    # st.write(selected_result)
    if selected_result:
        c_id= selected_result[0][0]
        brand=selected_result[0][1]
        rate= selected_result[0][2]

        # Layout of Create
    col1, col2,col3= st.columns(3)
    with col1:
        new_c_id = st.text_input("Cylinder Id:",c_id)
    with col2:
        new_brand = st.text_input("Brand:",brand)
    
    with col3:
        new_rate = st.text_input("Rate:",rate)
        
    if st.button("Update cylinder"):
        edit_details_cylinder(new_c_id,new_brand,new_rate,c_id,brand,rate)
        st.success("Successfully updated:: {} to ::{}".format(c_id, new_c_id))
    result2 = view_all_data_cylinder()
    df2 = pd.DataFrame(result2, columns=['c_id' ,'brand' , 'rate'])
    with st.expander("Updated data"):
        st.dataframe(df2)

def update_orders():
    result = view_all_data_orders()
    # st.write(result)
    df = pd.DataFrame(result, columns=['user_id','c_id' ,' inv_no' , 'date_of_order','quantity','amount'])
    with st.expander("Current orders"):
        st.dataframe(df)
    list_of_dealers = [i[0] for i in view_only_inv_no()]
    selected_dealer = st.selectbox("orders to Edit", list_of_dealers)
    selected_result = get_details_orders(selected_dealer)
    # st.write(selected_result)
    if selected_result:
        user_id= selected_result[0][0]
        c_id= selected_result[0][1]
        inv_no=selected_result[0][2]
        date_of_order= selected_result[0][3]
        quantity=selected_result[0][4]
        amount= selected_result[0][5]

        # Layout of Create

    col1, col2,col3= st.columns(3)
    with col1:
        new_user_id = st.text_input("User Id:",user_id)
        new_c_id = st.text_input("Cylinder Id:",c_id)
    with col2:
        new_inv_no = st.text_input("Invoice number:",inv_no)
        new_date_of_order = st.text_input("Date of order :",date_of_order)
    with col3:
        new_quantity = st.text_input("Quantity:",quantity)
        new_amount = st.text_input("Amount :",amount)
        
    if st.button("Update orders"):
        edit_details_orders(new_user_id,new_c_id,new_inv_no,new_date_of_order,new_quantity,new_amount,user_id,c_id,inv_no,date_of_order,quantity,amount)
        st.success("Successfully updated:: {} to ::{}".format(inv_no, new_inv_no))
    result2 = view_all_data_orders()
    df2 = pd.DataFrame(result2, columns=['user_id','c_id' ,' inv_no' , 'date_of_order','quantity','amount'])
    with st.expander("Updated data"):
        st.dataframe(df2)

def update_payment():
    result = view_all_data_payment()
    # st.write(result)
    df = pd.DataFrame(result, columns=['inv_no','transaction_id' ,'status' , 'date_of_payment'])
    with st.expander("Current payment"):
        st.dataframe(df)
    list_of_dealers = [i[0] for i in view_only_transaction_ids()]
    selected_dealer = st.selectbox("payment to Edit", list_of_dealers)
    selected_result = get_details_payment(selected_dealer)
    # st.write(selected_result)
    if selected_result:
        inv_no= selected_result[0][0]
        transaction_id= selected_result[0][1]
        status=selected_result[0][2]
        date_of_payment= selected_result[0][3]

        # Layout of Create

    col1, col2,col3,col4= st.columns(4)
    with col1:
        new_inv_no = st.text_input("Invoice No:",inv_no)
       
    with col2:
        new_transaction_id = st.text_input("Transaction Id:",transaction_id)
   
    with col3:
        new_status = st.text_input("Payment Status:",status)
  
    with col4:
        new_date_of_payment = st.text_input("Date of payment:",date_of_payment)
        
    if st.button("Update payment"):
        edit_details_payment(new_inv_no,new_transaction_id,new_status,new_date_of_payment,inv_no,transaction_id,status,date_of_payment)
        st.success("Successfully updated:: {} to ::{}".format(transaction_id, new_transaction_id))
    result2 = view_all_data_payment()
    df2 = pd.DataFrame(result2, columns=['inv_no','transaction_id' ,'status' , 'date_of_payment'])
    with st.expander("Updated data"):
        st.dataframe(df2)

def update_delivery():
    result = view_all_data_delivery()
    # st.write(result)
    df = pd.DataFrame(result, columns=['d_id','transaction_id' ,'del_staff' ,'phone_no', 'date_of_delivery'])
    with st.expander("Current delivery"):
        st.dataframe(df)
    list_of_dealers = [i[0] for i in view_only_d_ids()]
    selected_dealer = st.selectbox("delivery to Edit", list_of_dealers)
    selected_result = get_details_delivery(selected_dealer)
    # st.write(selected_result)
    if selected_result:
        d_id = selected_result[0][0]
        transaction_id = selected_result[0][1]
        del_staff = selected_result[0][2]
        phone_no = selected_result[0][3]
        date_of_delivery = selected_result[0][4]

        # Layout of Create
    d_id=1

    col1, col2,col3,col4,col5= st.columns(5)

    with col1:

        new_d_id = st.text_input("Delivery id:",d_id)
       
    with col2:

        new_transaction_id = st.text_input("Transaction Id:",transaction_id)
   
    with col3:
        
        new_del_staff = st.text_input("Delivery staff name:",del_staff)
  
    with col4:
        
        new_phone_no = st.text_input("Phone number:",phone_no)
    
    with col5:
      
       new_date_of_delivery= st.text_input("Date of delivery:",date_of_delivery)
        
    if st.button("Update delivery"):
        edit_details_delivery(new_d_id,new_transaction_id,new_del_staff,new_phone_no,new_date_of_delivery,d_id,transaction_id,del_staff,phone_no,date_of_delivery)
        st.success("Successfully updated:: {} to ::{}".format(d_id, new_d_id))
    result2 = view_all_data_delivery()
    df2 = pd.DataFrame(result2, columns=['d_id','transaction_id' ,'del_staff' ,'phone_no', 'date_of_deivery'])
    with st.expander("Updated data"):
        st.dataframe(df2)