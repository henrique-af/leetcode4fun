SELECT
    patient_id,
    patient_name,
    conditions
FROM
    Patients
WHERE
    conditions IS NOT NULL
    AND (
        INSTR(conditions, ' DIAB1') > 0
        OR SUBSTR(conditions, 1, 5) = 'DIAB1'
    )