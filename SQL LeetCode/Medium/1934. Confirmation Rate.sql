SELECT
    s.user_id,
    ROUND(
        NVL(
            AVG(
                CASE
                    WHEN c.action = 'confirmed' THEN 1.0
                    ELSE 0.0
                END
            ),
            0.0
        ),
        2
    ) AS confirmation_rate
FROM
    SIGNUPS S
    LEFT JOIN CONFIRMATIONS C ON s.user_id = c.user_id
GROUP BY
    s.user_id;