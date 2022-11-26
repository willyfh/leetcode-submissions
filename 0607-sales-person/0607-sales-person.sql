# Write your MySQL query statement below
select name from salesperson where name not in (select S.name from Orders O join Company C on O.com_id = C.com_id join SalesPerson S on O.sales_id=S.sales_id where C.name = 'RED')

