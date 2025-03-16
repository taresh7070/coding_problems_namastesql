select
c.category_name,
sum(coalesce(s.amount, 0)) as total_sales
from categories c
left join sales s
on c.category_id=s.category_id
group by 1
order by total_sales