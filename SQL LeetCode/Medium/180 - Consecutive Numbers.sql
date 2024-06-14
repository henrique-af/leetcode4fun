WITH ABC AS (
    SELECT
        ID,
        NUM,
        ID - DENSE_RANK() OVER(
            PARTITION BY NUM
            ORDER BY
                ID
        ) AS RN
    FROM
        Logs
)
SELECT
    DISTINCT NUM AS CONSECUTIVENUMS
FROM
    ABC
GROUP BY
    NUM,
    RN
HAVING
    COUNT(RN) >= 3;