SELECT
    p.project_id,
    ROUND(AVG(COALESCE(e.experience_years, 0)), 2) AS average_years
FROM
    Project p
    LEFT JOIN Employee e ON e.employee_id = p.employee_id
GROUP BY
    p.project_id
ORDER BY
    p.project_id ASC;