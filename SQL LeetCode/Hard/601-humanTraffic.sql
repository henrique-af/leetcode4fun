WITH numbered_rows AS (
  SELECT 
    id,
    visit_date,
    people,
    id - ROW_NUMBER() OVER (ORDER BY id) AS grp
  FROM stadium
  WHERE people >= 100
),
grouped_rows AS (
  SELECT grp
  FROM numbered_rows
  GROUP BY grp
  HAVING COUNT(*) >= 3
)
SELECT 
  s.id,
  SUBSTR(s.visit_date, 1, 10) AS visit_date,
  s.people
FROM stadium s
JOIN numbered_rows nr ON s.id = nr.id
WHERE nr.grp IN (SELECT grp FROM grouped_rows)
ORDER BY s.id