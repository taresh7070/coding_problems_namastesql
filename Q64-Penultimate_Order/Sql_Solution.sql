with cte as(select 
*,
RANK() over(partition by customer_name order by order_date desc) rw,
count(order_id) over(partition by customer_name) cnt
from orders)


select 
order_id ,
order_date,
customer_name,
product_name,
sales
from cte 
where 
rw=2 
or cnt=1
order by customer_name
