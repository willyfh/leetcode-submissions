# Write your MySQL query statement below
select A.id as id from Weather A, Weather B where A.temperature > B.temperature and datediff(A.recordDate, B.recordDate) = 1