# Write your MySQL query statement below
select name from salesperson where sales_id not in (select O.sales_id from Orders O join Company C on O.com_id = C.com_id where C.name = 'RED')

