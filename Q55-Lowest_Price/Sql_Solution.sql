
select
prd.category,
coalesce(min(case when pur.id is not null then prd.price end), 0) AS price
from products prd
left join purchases pur
on prd.id=pur.product_id and pur.stars>3
group by 1
order by category