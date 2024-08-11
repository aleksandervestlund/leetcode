# Write your MySQL query statement below
SELECT name AS Customers
FROM Customers LEFT OUTER JOIN Orders
ON Customers.id = Orders.customerId
WHERE customerId IS NULL;
