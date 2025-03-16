select
category,
sum(amount) total_sales
from sales
where EXTRACT(MONTH FROM order_date)=2
AND EXTRACT(YEAR FROM order_date)=2022
AND DAYOFWEEK(order_date) NOT IN (1,7)
group by 1
order by total_sales