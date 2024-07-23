/* Write your PL/SQL query statement below */
SELECT
    user_id,
    CONCAT(
        UPPER(SUBSTR(name, 0, 1)),
        LOWER(SUBSTR(name, 2))
    ) as name
FROM
    Users
ORDER BY
    user_id