SELECT
    class
FROM
    (
        SELECT
            c.class,
            COUNT(c.class) count
        FROM
            Courses c
        GROUP BY
            c.class
    )
WHERE
    count >= 5