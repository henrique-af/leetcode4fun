WITH RankedSalaries AS (
    SELECT
        e.name AS Employee,
        e.salary AS Salary,
        d.name AS Department,
        RANK() OVER (
            PARTITION BY e.departmentId
            ORDER BY
                e.salary DESC
        ) AS SalaryRank
    FROM
        Employee e
        INNER JOIN Department d ON e.departmentId = d.id
),
TopThreeSalaries AS (
    SELECT
        Employee,
        Salary,
        Department
    FROM
        RankedSalaries
    WHERE
        SalaryRank <= 3
)
SELECT
    Department,
    Employee,
    Salary
FROM
    TopThreeSalaries;