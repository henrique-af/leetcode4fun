SELECT
    num
FROM
(
        SELECT
            n.num,
            count(n.num) count
        FROM
            MyNumbers n
        GROUP BY
            n.num
    )
WHERE
    count = 1