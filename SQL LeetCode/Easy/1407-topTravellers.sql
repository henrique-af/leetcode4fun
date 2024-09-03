WITH UserDistances AS (
    SELECT
        s.name,
        COALESCE(SUM(r.distance), 0) AS travelled_distance
    FROM
        Users s
        LEFT JOIN Rides r ON r.user_id = s.id
    GROUP BY
        s.name,
        s.id
)
SELECT
    name,
    travelled_distance
FROM
    UserDistances
ORDER BY
    travelled_distance DESC,
    name ASC;