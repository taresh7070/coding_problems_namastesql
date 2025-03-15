select
case when price<100 then 'Low Price'
	 when price>=100 and price <=500 then 'Medium Price'
     else 'High Price'
end as category,
count(product_id) cnt
from products
group by 1
order by cnt desc;