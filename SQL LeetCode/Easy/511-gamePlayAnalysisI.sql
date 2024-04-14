WITH FirstLogins AS (
    SELECT
        player_id,
        MIN(event_date) AS first_login
    FROM
        Activity
    GROUP BY
        player_id
),
ConsecutiveLogins AS (
    SELECT
        f.player_id
    FROM
        FirstLogins f
        INNER JOIN Activity a ON f.player_id = a.player_id
        AND a.event_date = f.first_login + INTERVAL '1 day'
    GROUP BY
        f.player_id
)
SELECT
    ROUND(
        CAST(COUNT(DISTINCT c.player_id) AS NUMERIC) / CAST(COUNT(DISTINCT f.player_id) AS NUMERIC),
        2
    ) AS fraction
FROM
    FirstLogins f
    LEFT JOIN ConsecutiveLogins c ON f.player_id = c.player_id;