import pandas as pd
import streamlit as st
from database import view_all_data_consumer, view_only_user_ids, delete_data_consumer,view_all_data_cylinder, view_only_c_ids, delete_data_cylinder,view_all_data_orders, view_only_inv_no, delete_data_orders,view_only_transaction_ids,view_all_data_payment,delete_data_payment,view_all_data_delivery, view_only_d_ids, delete_data_delivery


def delete_consumer():
    result = view_all_data_consumer()
    df = pd.DataFrame(result, columns=['user_id' ,' firstname' , 'lastname' , 'dob' , 'age' , 'street_address' , 'state' , 'phone_no'])
    with st.expander("Current data"):
        st.dataframe(df)

    list_of_dealers = [i[0] for i in view_only_user_ids()]
    selected_dealer = st.selectbox("Task to Delete", list_of_dealers)
    st.warning("Do you want to delete :{}".format(selected_dealer))
    if st.button("Delete CONSUMER"):
        delete_data_consumer(selected_dealer)
        st.success("CONSUMER has been deleted successfully")
    new_result = view_all_data_consumer()
    df2 = pd.DataFrame(new_result, columns=['user_id' ,' firstname' , 'lastname' , 'dob' , 'age' , 'street_address' , 'state' , 'phone_no'])
    with st.expander("Updated data"):
        st.dataframe(df2)

def delete_cylinder():
    result = view_all_data_cylinder()
    df = pd.DataFrame(result, columns=['c_id' ,' brand' , 'rate'])
    with st.expander("Current data"):
        st.dataframe(df)

    list_of_dealers = [i[0] for i in view_only_c_ids()]
    selected_dealer = st.selectbox("Task to Delete", list_of_dealers)
    st.warning("Do you want to delete :{}".format(selected_dealer))
    if st.button("Delete cylinder"):
        delete_data_cylinder(selected_dealer)
        st.success("cylinder has been deleted successfully")
    new_result = view_all_data_cylinder()
    df2 = pd.DataFrame(new_result, columns=['c_id' ,' brand' , 'rate'])
    with st.expander("Updated data"):
        st.dataframe(df2)

def delete_orders():
    result = view_all_data_orders()
    df = pd.DataFrame(result, columns=['user_id','c_id' ,' inv_no' , 'date_of_order','quantity','amount'])
    with st.expander("Current data"):
        st.dataframe(df)

    list_of_dealers = [i[0] for i in view_only_inv_no()]
    selected_dealer = st.selectbox("Task to Delete", list_of_dealers)
    st.warning("Do you want to delete :{}".format(selected_dealer))
    if st.button("Delete orders"):
        delete_data_orders(selected_dealer)
        st.success("orders has been deleted successfully")
    new_result = view_all_data_orders()
    df2 = pd.DataFrame(new_result, columns=['user_id','c_id' ,' inv_no' , 'date_of_order','quantity','amount'])
    with st.expander("Updated data"):
        st.dataframe(df2)

def delete_payment():
    result = view_all_data_payment()
    df = pd.DataFrame(result, columns=['inv_no','transaction_id' ,'status' , 'date_of_payment'])
    with st.expander("Current data"):
        st.dataframe(df)

    list_of_dealers = [i[0] for i in view_only_transaction_ids()]
    selected_dealer = st.selectbox("Task to Delete", list_of_dealers)
    st.warning("Do you want to delete :{}".format(selected_dealer))
    if st.button("Delete payment"):
        delete_data_payment(selected_dealer)
        st.success("payment has been deleted successfully")
    new_result = view_all_data_payment()
    df2 = pd.DataFrame(new_result, columns=['inv_no','transaction_id' ,'status' , 'date_of_payment'])
    with st.expander("Updated data"):
        st.dataframe(df2)

def delete_delivery():
    result = view_all_data_delivery()
    df = pd.DataFrame(result, columns=['d_id','transaction_id' ,'del_staff' ,'phone_no', 'date_of_delivery'])
    with st.expander("Current data"):
        st.dataframe(df)

    list_of_dealers = [i[0] for i in view_only_d_ids()]
    selected_dealer = st.selectbox("Task to Delete", list_of_dealers)
    st.warning("Do you want to delete :{}".format(selected_dealer))
    if st.button("Delete delivery"):
        delete_data_delivery(selected_dealer)
        st.success("delivery has been deleted successfully")
    new_result = view_all_data_delivery()
    df2 = pd.DataFrame(new_result,columns=['d_id','transaction_id' ,'del_staff' ,'phone_no', 'date_of_delivery'])
    with st.expander("Updated data"):
        st.dataframe(df2)