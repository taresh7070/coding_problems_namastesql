select
p.product_name,
sum(s.quantity*p.price) as total_sales_amount
from products p
join sales s
on p.product_id=s.product_id
group by 1
order by product_name