select
name
from employees
where coalesce(mentor_id, 0) <> 3