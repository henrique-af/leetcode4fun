-- Write your PostgreSQL query statement below
SELECT
    email
FROM
    (
        SELECT
            email,
            COUNT(email) AS count
        FROM
            Person
        GROUP BY
            email
    ) AS counted_emails
WHERE
    count > 1;