SELECT
    c.id,
    c.movie,
    c.description,
    c.rating
FROM
    Cinema c
WHERE
    (c.id / 2 != TRUNC(c.id / 2))
    AND c.description != 'boring'
ORDER BY
    c.rating DESC


SELECT
    c.id,
    c.movie,
    c.description,
    c.rating
FROM
    Cinema c
WHERE
    MOD(c.id, 2) = 1
    AND c.description != 'boring'
ORDER BY
    c.rating DESC;