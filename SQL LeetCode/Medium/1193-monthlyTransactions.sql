SELECT
    TO_CHAR(TO_DATE(t.trans_date, 'YYYY-MM-DD'), 'YYYY-MM') AS month,
    t.country,
    COUNT(*) AS trans_count,
    COUNT(
        CASE
            WHEN t.state = 'approved' THEN 1
        END
    ) AS approved_count,
    SUM(t.amount) AS trans_total_amount,
    COALESCE(
        SUM(
            CASE
                WHEN t.state = 'approved' THEN t.amount
            END
        ),
        0
    ) AS approved_total_amount
FROM
    Transactions t
GROUP BY
    TO_CHAR(TO_DATE(t.trans_date, 'YYYY-MM-DD'), 'YYYY-MM'),
    t.country;