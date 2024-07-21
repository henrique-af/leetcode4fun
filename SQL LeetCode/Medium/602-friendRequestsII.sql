WITH requester AS (
    SELECT
        requester_id AS id
    FROM
        RequestAccepted
),
accepter AS (
    SELECT
        accepter_id AS id
    FROM
        RequestAccepted
),
unionT AS (
    SELECT
        *
    FROM
        requester
    UNION
    ALL
    SELECT
        *
    FROM
        accepter
),
total AS (
    SELECT
        id,
        COUNT(*) AS num
    FROM
        unionT
    GROUP BY
        id
)
SELECT
    id,
    num
FROM
    (
        SELECT
            id,
            num
        FROM
            total
        ORDER BY
            num DESC
    )
WHERE
    ROWNUM = 1;