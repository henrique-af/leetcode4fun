WITH FirstOrders AS (
    SELECT
        customer_id,
        MIN(order_date) AS first_order_date
    FROM
        Delivery
    GROUP BY
        customer_id
),
ImmediateFirstOrders AS (
    SELECT
        d.customer_id,
        d.order_date,
        d.customer_pref_delivery_date
    FROM
        Delivery d
        JOIN FirstOrders fo ON d.customer_id = fo.customer_id
        AND d.order_date = fo.first_order_date
)
SELECT
    ROUND(
        COUNT(
            CASE
                WHEN order_date = customer_pref_delivery_date THEN 1
            END
        ) * 100.0 / COUNT(*),
        2
    ) AS immediate_percentage
FROM
    ImmediateFirstOrders;