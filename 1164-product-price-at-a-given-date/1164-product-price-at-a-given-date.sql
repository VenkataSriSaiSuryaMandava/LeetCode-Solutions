# Write your MySQL query statement below
SELECT DISTINCT p.product_id, IFNULL(l.new_price, 10) AS price
FROM Products p
LEFT JOIN  
(
    SELECT product_id, new_price
    FROM Products
    WHERE (product_id, change_date) IN 
    (
        SELECT product_id, MAX(change_date) AS change_date
        FROM Products
        WHERE change_date <= "2019-08-16"
        GROUP BY product_id
    )
) l ON p.product_id = l.product_id;