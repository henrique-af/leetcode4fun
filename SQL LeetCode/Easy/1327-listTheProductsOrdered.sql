/* Write your PL/SQL query statement below */
SELECT
    *
FROM
    (
        SELECT
            p.product_name,
            NVL(SUM(o.unit), 0) AS unit
        FROM
            Products p
            LEFT JOIN Orders o ON p.product_id = o.product_id
            AND TO_CHAR(o.order_date, 'YYYY-MM') = '2020-02'
        GROUP BY
            p.product_name
    )
WHERE
    unit >= 100
ORDER BY
    product_name;