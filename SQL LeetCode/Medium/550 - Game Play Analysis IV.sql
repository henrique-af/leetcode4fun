WITH FirstLogin AS (
    SELECT
        player_id,
        MIN(event_date) AS first_login_date
    FROM
        Activity
    GROUP BY
        player_id
),
NextDayLogin AS (
    SELECT
        fl.player_id
    FROM
        FirstLogin fl
        JOIN Activity a ON fl.player_id = a.player_id
        AND a.event_date = fl.first_login_date + 1
)
SELECT
    ROUND(
        COUNT(DISTINCT ndl.player_id) / COUNT(DISTINCT fl.player_id),
        2
    ) AS fraction
FROM
    FirstLogin fl
    LEFT JOIN NextDayLogin ndl ON fl.player_id = ndl.player_id;