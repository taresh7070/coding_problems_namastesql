/*
select * from orders;
select * from returns;
*/
with cte as(
select
ord.customer_name,
round(count(rtn.order_id)/count(ord.order_id), 2)*100 return_perc
/*count(ord.order_id) total_order,
count(rtn.order_id) total_return*/
from orders ord
left join returns rtn
on ord.order_id=rtn.order_id
group by ord.customer_name)

select * from cte
where return_perc>50
order by customer_name asc;