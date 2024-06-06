SELECT
    DISTINCT v.author_id id
FROM
    Views v
WHERE
    v.author_id = v.viewer_id
ORDER BY
    id ASC