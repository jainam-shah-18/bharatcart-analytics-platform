select
    order_id,
    count(*) as review_count,
    avg(review_score) as avg_review_score,
    max(review_score) as max_review_score,
    min(review_score) as min_review_score
from {{ ref('stg_order_reviews') }}
group by order_id