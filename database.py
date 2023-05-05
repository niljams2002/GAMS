# pip install mysql-connector-python
import mysql.connector


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="gas_agency_management"
)
c = mydb.cursor()


def create_table_consumer():
    c.execute('CREATE TABLE IF NOT EXISTS CONSUMER(user_id TEXT, firstname TEXT,  lastname TEXT, dob TEXT,age TEXT, street_address TEXT,state TEXT,phone_no TEXT)')


def add_data_consumer(user_id,firstname,lastname,dob,age,street_address,state,phone_no):
    c.execute('INSERT INTO CONSUMER(user_id , firstname , lastname , dob , age , street_address , state , phone_no) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)',
              (user_id,firstname,lastname,dob,age,street_address,state,phone_no))
    

    c.execute('call update__to__current__age()')
    mydb.commit()


def view_all_data_consumer():
    c.execute('SELECT * FROM CONSUMER')
    data = c.fetchall()
    return data


def view_only_user_ids():
    c.execute('SELECT user_id FROM CONSUMER')
    data = c.fetchall()
    return data


def get_details_consumer(user_id):
    c.execute('SELECT * FROM Consumer WHERE user_id="{}"'.format(user_id))
    data = c.fetchall()
    return data


def edit_details_consumer(new_user_id,new_firstname,new_lastname,new_dob,new_age,new_street_address,new_state,new_phone_no,user_id,firstname,lastname,dob,age,street_address,state,phone_no):
    user_id1=int(user_id)
    new_user_id1=int(new_user_id)
    c.execute("UPDATE CONSUMER SET user_id=%s, firstname=%s, lastname=%s, dob=%s, age=%s, street_address=%s, state=%s, phone_no=%s WHERE user_id=%s and firstname=%s and lastname=%s and dob=%s and age=%s and street_address=%s and state=%s and phone_no=%s", (int(new_user_id1),new_firstname,new_lastname,new_dob,new_age,new_street_address,new_state,new_phone_no,int(user_id1),firstname,lastname,dob,age,street_address,state,phone_no))
    mydb.commit()
    c.execute('SELECT * FROM CONSUMER WHERE user_id="{}"'.format(user_id))
    data = c.fetchall()
    return data


def delete_data_consumer(user_id):
    c.execute('DELETE FROM CONSUMER WHERE user_id="{}"'.format(user_id))
    mydb.commit()


def create_table_cylinder():
    c.execute('CREATE TABLE IF NOT EXISTS Cylinder(c_id TEXT, brand TEXT,  rate TEXT)')


def add_data_cylinder(c_id,brand,rate):
    c.execute('INSERT INTO Cylinder(c_id,brand,rate) VALUES (%s,%s,%s)',(c_id,brand,rate))
    mydb.commit()


def view_all_data_cylinder():
    c.execute('SELECT * FROM Cylinder')
    data = c.fetchall()
    return data


def view_only_c_ids():
    c.execute('SELECT c_id FROM Cylinder')
    data = c.fetchall()
    return data


def get_details_cylinder(c_id):
    c.execute('SELECT * FROM Cylinder WHERE c_id="{}"'.format(c_id))
    data = c.fetchall()
    return data


def edit_details_cylinder(new_c_id,new_brand,new_rate,c_id,brand,rate):
    c.execute("UPDATE Cylinder SET c_id=%s, brand=%s, rate=%s WHERE c_id=%s and brand=%s and rate=%s",(new_c_id,new_brand,new_rate,c_id,brand,rate))
    mydb.commit()
    c.execute('SELECT * FROM Cylinder WHERE c_id="{}"'.format(c_id))
    data = c.fetchall()
    return data


def delete_data_cylinder(c_id):
    c.execute('DELETE FROM Cylinder WHERE c_id="{}"'.format(c_id))
    mydb.commit()



def create_table_orders():
    c.execute('CREATE TABLE IF NOT EXISTS orders(user_id TEXT, c_id TEXT,  inv_no TEXT, date_of_order TEXT,quantity TEXT, amount TEXT)')


def add_data_orders(user_id,c_id,inv_no,date_of_order,quantity,amount):
    c.execute('INSERT INTO orders(user_id,c_id,inv_no,date_of_order,quantity,amount) VALUES (%s,%s,%s,%s,%s,%s)',
              (user_id,c_id,inv_no,date_of_order,quantity,amount))
    c.execute('call update_amount')
    mydb.commit()


def view_all_data_orders():
    c.execute('SELECT * FROM orders')
    data = c.fetchall()
    return data


def view_only_inv_no():
    c.execute('SELECT inv_no FROM orders')
    data = c.fetchall()
    return data


def get_details_orders(inv_no):
    c.execute('SELECT * FROM orders WHERE inv_no="{}"'.format(inv_no))
    data = c.fetchall()
    return data


def edit_details_orders(new_user_id,new_c_id,new_inv_no,new_date_of_order,new_quantity,new_amount,user_id,c_id,inv_no,date_of_order,quantity,amount):

    c.execute("UPDATE orders SET user_id=%s, c_id=%s, inv_no=%s, date_of_order=%s, quantity=%s, amount=%s WHERE user_id=%s and c_id=%s and inv_no=%s and date_of_order=%s and quantity=%s and amount=%s" , (new_user_id,new_c_id,new_inv_no,new_date_of_order,new_quantity,new_amount,user_id,c_id,inv_no,date_of_order,quantity,amount))
    mydb.commit()
    c.execute('SELECT * FROM orders WHERE inv_no="{}"'.format(inv_no))
    data = c.fetchall()
    return data


def delete_data_orders(inv_no):
    c.execute('DELETE FROM orders WHERE inv_no="{}"'.format(inv_no))
    mydb.commit()

def create_table_payment():
    c.execute('CREATE TABLE IF NOT EXISTS payment(inv_no TEXT,transaction_id TEXT, status TEXT,date_of_payment TEXT)')


def add_data_payment(inv_no,transaction_id,status,date_of_payment):
    c.execute('INSERT INTO payment(inv_no,transaction_id,status,date_of_payment) VALUES (%s,%s,%s,%s)',
              (inv_no,transaction_id,status,date_of_payment))
    mydb.commit()


def view_all_data_payment():
    c.execute('SELECT * FROM payment')
    data = c.fetchall()
    return data


def view_only_transaction_ids():
    c.execute('SELECT transaction_id FROM payment')
    data = c.fetchall()
    return data


def get_details_payment(transaction_id):
    c.execute('SELECT * FROM payment WHERE transaction_id="{}"'.format(transaction_id))
    data = c.fetchall()
    return data


def edit_details_payment(new_inv_no,new_transaction_id,new_status,new_date_of_payment,inv_no,transaction_id,status,date_of_payment):

    c.execute("UPDATE payment SET inv_no=%s,transaction_id=%s, status=%s, date_of_payment=%s WHERE inv_no=%s and transaction_id=%s and status=%s and date_of_payment=%s", (new_inv_no,new_transaction_id,new_status,new_date_of_payment,inv_no,transaction_id,status,date_of_payment))
    mydb.commit()
    c.execute('SELECT * FROM payment WHERE transaction_id="{}"'.format(transaction_id))
    data = c.fetchall()
    return data


def delete_data_payment(transaction_id):
    c.execute('DELETE FROM payment WHERE transaction_id="{}"'.format(transaction_id))
    mydb.commit()

def create_table_delivery():
    c.execute('CREATE TABLE IF NOT EXISTS delivery(d_id TEXT,transaction_id TEXT, del_staff TEXT,phone_no TEXT,date_of_delivery TEXT)')


def add_data_delivery(d_id,transaction_id,del_staff,phone_no,date_of_delivery):
    c.execute('INSERT INTO delivery(d_id,transaction_id,del_staff,phone_no,date_of_delivery) VALUES (%s,%s,%s,%s,%s)',
              (d_id,transaction_id,del_staff,phone_no,date_of_delivery))
    mydb.commit()


def view_all_data_delivery():
    c.execute('SELECT * FROM delivery')
    data = c.fetchall()
    return data


def view_only_d_ids():
    c.execute('SELECT d_id FROM delivery')
    data = c.fetchall()
    return data


def get_details_delivery(d_id):
    c.execute('SELECT * FROM delivery WHERE d_id="{}"'.format(d_id))
    data = c.fetchall()
    return data


def edit_details_delivery(new_d_id,new_transaction_id,new_del_staff,new_phone_no,new_date_of_delivery,d_id,transaction_id,del_staff,phone_no,date_of_delivery):

    c.execute("UPDATE delivery SET d_id=%s,transaction_id=%s, del_staff=%s,phone_no=%s,date_of_delivery=%s WHERE d_id=%s and transaction_id=%s and del_staff=%s and phone_no=%s and date_of_delivery=%s", (new_d_id,new_transaction_id,new_del_staff,new_phone_no,new_date_of_delivery,d_id,transaction_id,del_staff,phone_no,date_of_delivery))
    mydb.commit()
    c.execute('SELECT * FROM delivery WHERE d_id="{}"'.format(d_id))
    data = c.fetchall()
    return data


def delete_data_delivery(d_id):
    c.execute('DELETE FROM delivery WHERE d_id="{}"'.format(d_id))
    mydb.commit()