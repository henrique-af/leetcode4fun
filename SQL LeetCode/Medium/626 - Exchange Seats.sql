/* Write your PL/SQL query statement below */
WITH seat_pairs AS (
    SELECT
        CASE
            WHEN MOD(id, 2) = 1
            AND id + 1 <= (
                SELECT
                    MAX(id)
                FROM
                    Seat
            ) THEN id + 1
            WHEN MOD(id, 2) = 0 THEN id - 1
            ELSE id
        END AS new_id,
        student
    FROM
        Seat
)
SELECT
    new_id AS id,
    student
FROM
    seat_pairs
ORDER BY
    new_id ASC;