1

-----

Write a query that shows all the information about all the salespeople in
the database. Use a basic SELECT query.

-----


SELECT * FROM salespeople
;


==========
2

-----

Write a query that shows all the information about all salespeople from
the 'Northwest' region.

-----


SELECT * FROM salespeople WHERE region = 'Northwest'
;


==========
3

-----

Write a query that shows just the emails of the salespeople from the
'Southwest' region.

-----


SELECT email FROM salespeople WHERE region = 'Southwest'
;


==========
4

-----

Write a query that shows the first name, last name, and email of all
salespeople in the 'Northwest' region.

-----


SELECT first_name, last_name, email FROM salespeople WHERE region = 'Northwest';


==========
5

-----

Write a query that shows the common name of melons that cost more than
$5.00.

-----


SELECT common_name FROM melons WHERE price > 5;


==========
6

-----

Write a query that shows the common name and price for all
watermelons that cost more than $5.00.


-----


SELECT common_name, price FROM melons WHERE melon_type = 'Watermelon' AND price > 5
;


==========
7

-----

Write a query that displays all common names of melons that start with
the letter 'C'.


-----


SELECT common_name FROM melons WHERE common_name LIKE 'C%';


==========
8

-----

Write a query that shows the common name of any melon with 'Golden'
anywhere in the common name.


-----


SELECT common_name FROM melons WHERE common_name LIKE '%Golden%';


==========
9

-----

Write a query that shows all the distinct regions that a salesperson can belong to.


-----


SELECT DISTINCT region from salespeople;


==========
10

-----

Write a query that shows the emails of all salespeople from both the
Northwest and Southwest regions.


-----


SELECT email FROM salespeople WHERE region in ('Northwest', 'Southwest');


==========
11

-----

Write a query that shows the emails of all salespeople from both the
Northwest and Southwest regions, this time using an 'IN' clause.  


-----


SELECT email FROM salespeople WHERE region = 'Northwest' or region = 'Southwest';


==========
12

-----

Write a query that shows the email, first name, and last name of all
salespeople in either the Northwest or Southwest regions whose last names start
with the letter 'M'.

-----


SELECT email, first_name, last_name FROM salespeople WHERE region in ('Northwest', 'Southwest') AND last_name LIKE 'M%';


==========
13

-----

Write a query that shows the melon type, common name, price, and the
price of the melon given in euros. The 'melons' table has prices in dollars,
and the dollar to euro conversion rate is 0.73.


-----


SELECT melon_type, common_name, price, price * 0.73 as euros FROM melons;


==========
14

-----

Write a query that shows the total number of customers in our customer
table.

-----


SELECT count(*) FROM customers;


==========
15

-----

Write a query that counts the number of orders (in the orders table) shipped to California.

-----


SELECT count(*) FROM orders WHERE shipto_state = 'CA';


==========
16

-----

Write a query that shows the total amount of money spent across all melon
orders.

-----


SELECT SUM(order_total) FROM orders;


==========
17

-----

Write a query that shows the average order cost.

-----


SELECT AVG(order_total) FROM orders;


==========
18

-----

Write a query that shows the order total that was lowest in price.

-----


SELECT MIN(order_total) FROM orders;


==========
19

-----

Write a query that fetches the id of the customer whose email is
'pclark74@gmail.com'.

-----


SELECT id FROM customers WHERE email = 'pclark74@gmail.com'
;


==========
20

-----

Write a query that shows the id, status and order_total for all orders 
made by customer 100.

-----


SELECT id, status, order_total FROM orders WHERE customer_id = 100;


==========
21

-----

Write a single query that shows the id, status, and order total for all
orders made by 'pclark74@gmail.com'. Use a subselect to do this.


-----


SELECT id, status, order_total FROM orders WHERE customer_id = (SELECT id FROM customers WHERE email = 'pclark74@gmail.com');


==========
22

-----

Write a query that shows the id, status, and order total for all orders
made by 'pclark74@gmail.com'. Use a join to do this.

-----


SELECT orders.id, orders.status, orders.order_total
FROM orders JOIN customers
ON orders.customer_id = customers.id
WHERE customers.email = 'pclark74@gmail.com';


==========
23

-----

Write a query that shows all columns in the order_items table for order #2725.

-----


SELECT * FROM order_items WHERE order_id = 2725
;


==========
24

-----

Write a query that shows the common_name, melon_type, quantity,
unit_price and total_price for all the melons in order #2725.

-----


SELECT melons.common_name, melons.melon_type, order_items.quantity, order_items.unit_price, order_items.total_price
FROM melons JOIN order_items
ON melons.id = order_items.melon_id
WHERE order_items.order_id = 2725;


==========
25

-----

Write a query that shows the total amount of revenue that comes from
internet orders.

-----


SELECT SUM(order_total) FROM orders WHERE salesperson_id IS NULL;


==========
26

-----

Challenge: Produce a list of all salespeople and the total amount of orders
they've sold, while calculating a 15% commission on all of their orders.
Include their first name, last name, the total of all their sales, and their
commission. Only report one row per salesperson. Include salespeople who have
not made any sales.

You will need 'left join' (http://sqlzoo.net/wiki/LEFT_JOIN) and 'group by'
(http://sqlzoo.net/wiki/SELECT_.._GROUP_BY) clauses to finish this one.

-----


SELECT first_name, last_name, sales, commission FROM salespeople LEFT JOIN (SELECT salesperson_id, SUM(order_total) as sales, SUM(order_total * .15) as commission FROM orders GROUP BY salesperson_id) as orders ON salespeople.id = orders.salesperson_id;