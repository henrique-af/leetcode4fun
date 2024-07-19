SELECT
    TO_CHAR(c.visited_on, 'YYYY-MM-DD') AS visited_on,
    (
        SELECT
            SUM(c2.amount)
        FROM
            customer c2
        WHERE
            c2.visited_on BETWEEN c.visited_on - INTERVAL '6' DAY
            AND c.visited_on
    ) AS amount,
    ROUND(
        (
            SELECT
                SUM(c2.amount) / 7
            FROM
                customer c2
            WHERE
                c2.visited_on BETWEEN c.visited_on - INTERVAL '6' DAY
                AND c.visited_on
        ),
        2
    ) AS average_amount
FROM
    customer c
WHERE
    c.visited_on >= (
        SELECT
            MIN(c2.visited_on) + INTERVAL '6' DAY
        FROM
            customer c2
    )
GROUP BY
    c.visited_on
ORDER BY
    c.visited_on;