WITH distinct_activities AS (
    SELECT
        TO_CHAR(TO_DATE(sell_date, 'yyyy-mm-dd'), 'yyyy-mm-dd') AS sell_date,
        product
    FROM
        Activities
    GROUP BY
        TO_CHAR(TO_DATE(sell_date, 'yyyy-mm-dd'), 'yyyy-mm-dd'),
        product
)
SELECT
    sell_date,
    COUNT(product) AS num_sold,
    LISTAGG(product, ',') WITHIN GROUP (
        ORDER BY
            product
    ) AS products
FROM
    distinct_activities
GROUP BY
    sell_date
ORDER BY
    sell_date;