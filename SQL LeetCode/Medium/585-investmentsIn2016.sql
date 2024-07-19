WITH SharedTiv2015 AS (
    SELECT
        tiv_2015
    FROM
        Insurance
    GROUP BY
        tiv_2015
    HAVING
        COUNT(*) > 1
),
UniqueCities AS (
    SELECT
        lat,
        lon
    FROM
        Insurance
    GROUP BY
        lat,
        lon
    HAVING
        COUNT(*) = 1
),
FilteredPolicies AS (
    SELECT
        i.tiv_2016
    FROM
        Insurance i
        JOIN SharedTiv2015 s ON i.tiv_2015 = s.tiv_2015
        JOIN UniqueCities u ON i.lat = u.lat
        AND i.lon = u.lon
)
SELECT
    ROUND(SUM(tiv_2016), 2) AS tiv_2016
FROM
    FilteredPolicies;