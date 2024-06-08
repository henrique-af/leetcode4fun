/* WRITE YOUR PL/SQL QUERY STATEMENT BELOW */
SELECT
    E.NAME,
    B.BONUS
FROM
    EMPLOYEE E
    LEFT JOIN BONUS B ON E.EMPID = B.EMPID
WHERE
    B.BONUS NOT IN (
        SELECT
            B.BONUS
        FROM
            BONUS B
        WHERE
            B.BONUS >= '1000'
    )
    OR BONUS IS NULL;