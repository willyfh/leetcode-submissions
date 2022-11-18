# Write your MySQL query statement below

SELECT firstName, lastName, city, state  from Person P LEFT JOIN Address A ON P.personId=A.personId