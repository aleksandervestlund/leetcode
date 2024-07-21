# Write your MySQL query statement below
SELECT firstName, lastName, city, state
FROM Person LEFT OUTER JOIN Address USING (personId);