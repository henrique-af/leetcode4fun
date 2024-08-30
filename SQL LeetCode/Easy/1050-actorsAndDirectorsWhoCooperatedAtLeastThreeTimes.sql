WITH count_actor AS (
    SELECT
        actor_id,
        director_id,
        count(director_id) AS director_count
    FROM
        ActorDirector
    GROUP BY
        actor_id, director_id
)
SELECT
    actor_id,
    director_id
FROM
    count_actor
WHERE
    director_count >= 3