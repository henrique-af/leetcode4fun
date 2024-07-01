/* Write your PL/SQL query statement below */
WITH managers AS (
    SELECT
        DISTINCT manager_id
    FROM
        Employees
    WHERE
        manager_id IS NOT NULL
        AND manager_id NOT IN (
            SELECT
                employee_id
            FROM
                Employees
        )
)
SELECT
    e.employee_id
FROM
    Employees e
    JOIN managers m ON e.manager_id = m.manager_id
WHERE
    e.salary < 30000
ORDER BY
    e.employee_id;