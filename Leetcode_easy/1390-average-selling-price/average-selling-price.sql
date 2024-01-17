# Write your MySQL query statement below
select p.product_id, IFNULL(ROUND(SUM(p.price*units)/SUM(us.units),2),0) AS average_price
FROM Prices as p
LEFT JOIN UnitsSold AS us
ON p.product_id = us.product_id AND us.purchase_date BETWEEN p.start_date and 
p.end_date
GROUP BY p.product_id;