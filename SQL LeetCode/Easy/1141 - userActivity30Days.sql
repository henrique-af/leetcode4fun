SELECT
    TO_CHAR(a.activity_date, 'YYYY-MM-DD') AS day,
    COUNT(DISTINCT a.user_id) AS active_users
FROM
    Activity a
WHERE
    a.activity_date BETWEEN DATE '2019-06-28'
    AND DATE '2019-07-27'
GROUP BY
    TO_CHAR(a.activity_date, 'YYYY-MM-DD')
ORDER BY
    day;