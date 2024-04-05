WITH p AS (
    SELECT
        personId,
        lastName,
        firstName
    FROM
        Person
)
SELECT
    p.firstName,
    p.lastName,
    a.city,
    a.state
FROM
    p
    LEFT JOIN Address a ON p.personId = a.personId;