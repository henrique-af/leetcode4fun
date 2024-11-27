WITH unbanned_trips AS (
    SELECT 
        t.request_at,
        CASE WHEN t.Status LIKE 'cancelled%' THEN 1 ELSE 0 END AS is_cancelled
    FROM
        Trips t
    JOIN
        Users c ON t.client_id = c.users_id
    JOIN
        Users d ON t.driver_id = d.users_id
    WHERE
        t.request_at BETWEEN '2013-10-01' AND '2013-10-03'
        AND c.banned = 'No'
        AND d.banned = 'No'
)
SELECT 
    Request_at AS "Day",
    ROUND(SUM(is_cancelled) / COUNT(*), 2) AS "Cancellation Rate"
FROM unbanned_trips
GROUP BY Request_at
ORDER BY Request_at