
/*
with cte as 
(
  select 
  (o.order_date - p.price_date) as diff,
  rank() over(partition by o.order_id order by (o.order_date - p.price_date)) rnk,
  p.*,
  o.order_id,
  o.order_date
  from products p
  join orders o
  on p.product_id=o.product_id
  where 
  (o.order_date - p.price_date)>=0
)

select 
product_id, 
sum(price) as total_sales
from cte 
where rnk=1
group by 1

*/


with price_cte as (
select
product_id,
price,
price_date AS start_date,
lead(price_date, 1, '9999-12-31') over(partition by product_id order by price_date) AS end_date
from products
)


select
o.product_id,
sum(p.price)
from
orders o
join price_cte p
on o.product_id=p.product_id 
and o.order_date>=p.start_date
and o.order_date<p.end_date
group by 1