# Write your MySQL query statement below
SELECT name, bonus
FROM Employee LEFT OUTER JOIN Bonus
    USING (empId)
WHERE bonus IS NULL OR bonus < 1000;
