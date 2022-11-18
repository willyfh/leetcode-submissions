# Write your MySQL query statement below

SELECT Employee FROM (SELECT A.name as Employee, A.salary as Salary, B.salary ManagerSalary FROM Employee A JOIN Employee B ON A.managerId = B.id) T WHERE T.Salary > T.ManagerSalary