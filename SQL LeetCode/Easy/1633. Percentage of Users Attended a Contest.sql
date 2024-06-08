SELECT
    r.contest_id,
    CASE
        WHEN COUNT(r.user_id) = (
            SELECT
                COUNT(user_id)
            FROM
                Users
        ) THEN 100
        ELSE ROUND(
            COUNT(r.user_id) / (
                SELECT
                    COUNT(user_id)
                FROM
                    Users
            ) * 100,
            2
        )
    END AS percentage
FROM
    Register r
GROUP BY
    r.contest_id
ORDER BY
    CASE
        WHEN COUNT(r.user_id) = (
            SELECT
                COUNT(user_id)
            FROM
                Users
        ) THEN 100
        ELSE ROUND(
            COUNT(r.user_id) / (
                SELECT
                    COUNT(user_id)
                FROM
                    Users
            ) * 100,
            2
        )
    END DESC,
    r.contest_id ASC;