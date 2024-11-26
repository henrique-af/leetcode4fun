WITH buy AS (
    SELECT
        stock_name,
        SUM(price) AS price_buy
    FROM
        Stocks
    WHERE 
        operation = 'Buy'
    GROUP BY 
        stock_name
), 
loss AS (
    SELECT    
        stock_name,
        SUM(price) AS price_loss
    FROM
        Stocks
    WHERE 
        operation = 'Sell'
    GROUP BY 
        stock_name
)
SELECT 
    b.stock_name, 
    COALESCE(b.price_buy, 0) - COALESCE(l.price_loss, 0) AS price_difference
FROM 
    buy b
LEFT JOIN 
    loss l ON b.stock_name = l.stock_name;

SELECT 
    stock_name,
    SUM(CASE WHEN operation = 'Sell' THEN price ELSE 0 END) 
    - SUM(CASE WHEN operation = 'Buy' THEN price ELSE 0 END) AS capital_gain_loss
FROM 
    Stocks
GROUP BY 
    stock_name;

