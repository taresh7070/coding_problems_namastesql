select * from product_reviews
  where 
  UPPER(TRIM(review_text)) not like '%NOT_EXCELLENT%' 
  and UPPER(TRIM(review_text)) not like '%NOT_AMAZING%'
  AND (UPPER(TRIM(review_text)) like '%EXCELLENT%' or UPPER(TRIM(review_text)) like '%AMAZING%')