SELECT
    C.CUSTOMER_ID
FROM
    CUSTOMER C
    LEFT JOIN PRODUCT P ON C.PRODUCT_KEY = P.PRODUCT_KEY
    GROUP BY
    C.CUSTOMER_ID
HAVING
    COUNT(DISTINCT C.PRODUCT_KEY) = (
        SELECT
            COUNT(*)
        FROM
            PRODUCT P
    )