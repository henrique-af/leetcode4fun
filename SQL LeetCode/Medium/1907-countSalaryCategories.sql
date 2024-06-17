WITH LowSalary AS (
    SELECT
        account_id
    FROM
        Accounts
    WHERE
        income < 20000
),
AverageSalary AS (
    SELECT
        account_id
    FROM
        Accounts
    WHERE
        income BETWEEN 20000
        AND 50000
),
HighSalary AS (
    SELECT
        account_id
    FROM
        Accounts
    WHERE
        income > 50000
)
SELECT
    'Low Salary' AS category,
    COUNT(account_id) AS accounts_count
FROM
    LowSalary
UNION
ALL
SELECT
    'Average Salary' AS category,
    COUNT(account_id) AS accounts_count
FROM
    AverageSalary
UNION
ALL
SELECT
    'High Salary' AS category,
    COUNT(account_id) AS accounts_count
FROM
    HighSalary;