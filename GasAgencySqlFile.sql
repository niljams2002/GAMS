Create table consumer (
user_id int(20) NOT NULL,
firstname varchar(50),
lastname varchar(50),
dob Date,
age int,
street_address varchar(50),	
state varchar(50),
phone_no varchar(20),
PRIMARY KEY(user_id));

Create table cylinder(
c_id int(10) NOT NULL,
brand varchar(20),
rate int(10),
PRIMARY KEY(c_id));

Create table orders(
user_id int(10) NOT NULL,
c_id int(10) NOT NULL,
inv_no int(10) NOT NULL,
date_of_order Date,	
quantity int(10),
amount int(10),
Foreign key (user_id) references consumer(user_id),
Foreign key (c_id) references cylinder(c_id),
PRIMARY KEY(inv_no));

Create table payment(
inv_no int(10) NOT NULL,
transaction_id varchar(10) NOT NULL,
status varchar(20),
date_of_payment Date,
Foreign key (inv_no) references orders(inv_no),
PRIMARY KEY(transaction_id));

Create table delivery(
d_id int(10) NOT NULL,
transaction_id varchar(10),
del_staff varchar(20),
phone_no varchar(20),
date_of_delivery Date,
Foreign key (transaction_id) references payment (transaction_id),
PRIMARY KEY(d_id));


insert into consumer values(1,"Kevin","Jacob","1971-01-01",NULL,"10 Janpath","Karnataka","9845042491");
insert into cylinder values(101,"hp",800);
insert into orders values(1,101,10001,"2022-01-10",5,0);
insert into payment values(10001,"A1200","Not paid","2022-01-10");
insert into delivery values(1,"A1200","Kuval","9876543210","2002-02-06");

insert into consumer(user_id,firstname,lastname,dob,age,street_address,state,phone_no) values(2,"Kavisha","Mathur","2000-10-09",NULL,"10 Downing","Delhi","9945278900");

insert into cylinder(c_id,brand,rate) values(102,"bharat",850);


insert into orders(user_id,c_id,inv_no,date_of_order,quantity,amount) values(2,101,10002,"2022-02-04",2,0);


insert into payment(inv_no,transaction_id,status,date_of_payment)values(10002,"B1000","Not paid","2022-02-04");

insert into delivery (d_id,transaction_id,del_staff,phone_no,date_of_delivery) values(2,"B1000","Kunal","1234567890","2002-03-13");

LOAD DATA INFILE "C:\\Users\\KEVIN\\Desktop\\GAS_AGENCY\\Consumer.csv" INTO TABLE consumer
COLUMNS TERMINATED BY ','
OPTIONALLY ENCLOSED BY " "
ESCAPED BY ""
LINES TERMINATED BY '\n'
IGNORE 3 LINES
(user_id,firstname,lastname,@DOB,age,street_address,state,phone_no)
SET DOB = STR_TO_DATE(@DOB, '%d-%m-%Y');

LOAD DATA INFILE "C:\\Users\\KEVIN\\Desktop\\GAS_AGENCY\\Cylinder.csv" INTO TABLE cylinder
COLUMNS TERMINATED BY ','
OPTIONALLY ENCLOSED BY " "
ESCAPED BY ""
LINES TERMINATED BY '\n'
IGNORE 3 LINES;

LOAD DATA INFILE "C:\\Users\\KEVIN\\Desktop\\GAS_AGENCY\\Order.csv" INTO TABLE orders
COLUMNS TERMINATED BY ','
OPTIONALLY ENCLOSED BY " "
ESCAPED BY ""
LINES TERMINATED BY '\n'
IGNORE 3 LINES
(user_id,c_id,inv_no,@date_of_order,quantity,amount)
SET date_of_order = STR_TO_DATE(@Date_of_order, '%d-%m-%Y');

LOAD DATA INFILE "C:\\Users\\KEVIN\\Desktop\\GAS_AGENCY\\Payment.csv" INTO TABLE payment
COLUMNS TERMINATED BY ','
OPTIONALLY ENCLOSED BY " "
ESCAPED BY ""
LINES TERMINATED BY '\n'
IGNORE 3 LINES
(inv_no,transaction_id,status,@date_of_payment)
SET date_of_payment = STR_TO_DATE(@date_of_payment, '%d-%m-%Y');

LOAD DATA INFILE "C:\\Users\\KEVIN\\Desktop\\GAS_AGENCY\\Delivery.csv" INTO TABLE delivery
COLUMNS TERMINATED BY ','
OPTIONALLY ENCLOSED BY " "
ESCAPED BY ""
LINES TERMINATED BY '\n'
IGNORE 3 LINES
(d_id,transaction_id,del_staff,phone_no,@date_of_delivery)
SET date_of_delivery = STR_TO_DATE(@date_of_delivery, '%d-%m-%Y');

ALTER table orders modify column amount int NULL;

UPDATE orders INNER JOIN cylinder ON orders.c_id=cylinder.c_id SET orders.amount=orders.quantity*cylinder.rate WHERE orders.c_id=cylinder.c_id;



SELECT DISTINCT user_id,firstname FROM consumer NATURAL JOIN orders;



SELECT DISTINCT c_id,brand,rate FROM cylinder NATURAL JOIN orders;



select transaction_id,amount from payment left join orders on orders.inv_no=payment.inv_no WHERE status="Paid"; 


select avg(rate) as 
Average_Rate_of_Cylinders from cylinder;


SELECT consumer.* FROM consumer INNER JOIN (SELECT MAX(age) Age FROM consumer) maxAge on consumer.Age = maxAge.Age;

SELECT consumer.* FROM consumer INNER JOIN (SELECT MIN(age) Age FROM consumer) mINAge on consumer.Age = mINAge.Age;


Select sum(amount) as SUM_OF_ORDERS from orders;


SELECT consumer.* FROM consumer WHERE user_id=1 UNION SELECT consumer.* FROM consumer WHERE user_id=2;


SELECT consumer.* FROM consumer WHERE user_id=1 UNION ALL SELECT consumer.* FROM consumer WHERE user_id=2;


SELECT consumer.phone_no FROM consumer UNION  SELECT delivery.phone_no FROM delivery;


SELECT date_of_payment FROM payment INTERSECT SELECT date_of_delivery FROM delivery;


SELECT date_of_payment FROM payment INTERSECT SELECT date_of_order FROM orders;

SELECT date_of_order FROM orders INTERSECT SELECT date_of_delivery FROM delivery;

select * from consumer;
DELIMITER $$
CREATE procedure update__to__current__age()
BEGIN
DECLARE c DATE;
SELECT sysdate() into c;
update consumer 
SET age=year(c)-year(dob);
END;$$
DELIMITER ;
call update__to__current__age();
select * from consumer;

DELIMITER $$
CREATE FUNCTION high_amounts(amount int (10))
RETURNS varchar(100) 
DETERMINISTIC
BEGIN DECLARE n int default 0;
DECLARE msg varchar(100);
select count(amount) into n from orders where amount>(SELECT avg(amount) FROM orders);
if n>3 then set msg:= "3 or more orders are of high amounts"; 
else set msg:= concat("We have only ",3-n," high amount orders"); 
end if; 
RETURN msg; 
END;$$
DELIMITER ;
select distinct high_amounts(orders.amount) from orders;


DELIMITER $$
CREATE TRIGGER date_delivery
BEFORE INSERT ON delivery
FOR EACH ROW
BEGIN
  IF NEW.date_of_delivery > CURRENT_DATE()
  THEN
   SIGNAL SQLSTATE '02000' SET MESSAGE_TEXT = 'Warning: delivery can not be greater than current date!';
  END IF;

END$$
    DELIMITER ;
DELIMITER $$
CREATE TRIGGER date_payment
BEFORE INSERT ON payment
FOR EACH ROW
BEGIN
  IF NEW.date_of_payment > CURRENT_DATE()
  THEN
   SIGNAL SQLSTATE '02000' SET MESSAGE_TEXT = 'Warning: payment date can not be greater than current date!';
  END IF;

END$$
    DELIMITER ;

DELIMITER $$
CREATE TRIGGER date_order
BEFORE INSERT ON orders
FOR EACH ROW
BEGIN
  IF NEW.date_of_order > CURRENT_DATE()
  THEN
   SIGNAL SQLSTATE '02000' SET MESSAGE_TEXT = 'Warning: order date can not be greater than current date!';
  END IF;

END$$
    DELIMITER ;





DELIMITER $$

create procedure update_amount()
BEGIN 

    DECLARE new_amount INT;
    DECLARE finished INT DEFAULT 0;
    DECLARE result CURSOR FOR
        SELECT amount FROM orders;
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET finished = 1;

    open result;
    result_loop: LOOP
        FETCH result INTO new_amount;
        IF finished = 1 THEN
            LEAVE result_loop;
        END IF;

	  UPDATE orders INNER JOIN cylinder ON orders.c_id=cylinder.c_id SET orders.amount=orders.quantity*cylinder.rate WHERE orders.c_id=cylinder.c_id;

    END LOOP result_loop;
    close result;

END $$

DELIMITER ;

insert into orders(user_id,c_id,inv_no,date_of_order,quantity,amount) values(2,101,10009,"2020-02-04",5,200);
insert into orders(user_id,c_id,inv_no,date_of_order,quantity,amount) values(2,101,100019,"2020-02-04",5,0);
select * from orders;
call update_amount();
select * from orders;


#test cases
insert into delivery (d_id,transaction_id,del_staff,phone_no,date_of_delivery) values(9,"B1000","Kunal","1234567890","2023-03-13");

insert into orders(user_id,c_id,inv_no,date_of_order,quantity,amount) values(2,101,10009,"2023-02-04",2,0);


insert into payment(inv_no,transaction_id,status,date_of_payment)values(10009,"Z1000","Not paid","2023-02-04");
