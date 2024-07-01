SELECT
    name AS results
FROM
    (
        SELECT
            u.name,
            dense_rank() OVER (
                ORDER BY
                    count(mr.created_at) DESC,
                    u.name ASC
            ) AS rnk
        FROM
            users u
            INNER JOIN movierating mr ON u.user_id = mr.user_id
        GROUP BY
            u.name
    ) A
WHERE
    rnk = 1
UNION
ALL
SELECT
    title AS results
FROM
    (
        SELECT
            title,
            dense_rank() OVER (
                ORDER BY
                    AVG(rating) DESC,
                    title ASC
            ) rnk
        FROM
            movies m
            INNER JOIN movierating mr ON m.movie_id = mr.movie_id
        WHERE
            TO_CHAR(mr.created_at, 'YYYY-MM') = '2020-02'
        GROUP BY
            title
    )
WHERE
    rnk = 1