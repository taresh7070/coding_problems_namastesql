select
d.department_name,
ROUND(AVG(e.salary), 2) average_salary
from departments d
join employees e
on d.department_id=e.department_id
group by 1
having count(employee_id)>2
order by average_salary desc