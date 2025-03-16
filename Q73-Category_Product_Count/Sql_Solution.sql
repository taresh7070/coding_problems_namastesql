select
category,
(LENGTH(products) - LENGTH(REPLACE(products, ',', '')) + 1) AS cnt
from categories
order by cnt