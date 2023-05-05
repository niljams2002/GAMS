import pandas as pd
import streamlit as st
import plotly.express as px
from database import view_all_data_consumer,view_all_data_cylinder,view_all_data_orders,view_all_data_payment,view_all_data_delivery


def read_consumer():
    result = view_all_data_consumer()
    # st.write(result)
    df = pd.DataFrame(result, columns=['user_id' ,' firstname' , 'lastname' , 'dob' , 'age' , 'street_address' , 'state' , 'phone_no'])
    with st.expander("View all Consumers"):
        st.dataframe(df)

def read_cylinder():
    result = view_all_data_cylinder()
    # st.write(result)
    df = pd.DataFrame(result, columns=['c_id' ,' brand' , 'rate'])
    with st.expander("View all Cylinders"):
        st.dataframe(df)

def read_orders():
    result = view_all_data_orders()
    # st.write(result)
    df = pd.DataFrame(result, columns=['user_id','c_id' ,' inv_no' , 'date_of_order','quantity','amount'])
    with st.expander("View all Orders"):
        st.dataframe(df)

def read_payment():
    result = view_all_data_payment()
    # st.write(result)
    df = pd.DataFrame(result, columns=['inv_no','transaction_id' ,'status' , 'date_of_payment'])
    with st.expander("View all Payments"):
        st.dataframe(df)

def read_delivery():
    result = view_all_data_delivery()
    # st.write(result)
    df = pd.DataFrame(result, columns=['d_id','transaction_id' ,'del_staff' ,'phone_no', 'date_of_delivery'])
    with st.expander("View all Delivery"):
        st.dataframe(df)