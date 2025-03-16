with payment_cte as
(
  select
	loan_id,
	sum(amount_paid) total_amount_paid,
	max(payment_date) mx_payment_date
  from Payments
  group by 1
)

select
l.loan_id,
l.loan_amount,
l.due_date,
case 
	when p.total_amount_paid=l.loan_amount 
    then 1 
    else 0 
end AS fully_paid_flag,
case 
	when p.total_amount_paid=l.loan_amount 
    AND p.mx_payment_date<=l.due_date 
    then 1 
    else 0 
end AS on_time_flag
from loans l
join payment_cte p
on l.loan_id=p.loan_id
