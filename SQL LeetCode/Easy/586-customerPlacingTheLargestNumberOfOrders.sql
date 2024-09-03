WITH count AS (
    SELECT
        customer_number,
        COUNT(customer_number) AS count
    FROM
        Orders
    GROUP BY
        customer_number
)
SELECT
    o.customer_number
FROM
    Count o
WHERE
    o.count = (
        SELECT
            MAX(count)
        FROM
            count
    );