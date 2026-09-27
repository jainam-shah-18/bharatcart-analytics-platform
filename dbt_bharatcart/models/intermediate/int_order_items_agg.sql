select
    order_id,
    count(*) as item_count,
    count(distinct product_id) as distinct_product_count,
    count(distinct seller_id) as seller_count,
    sum(price) as total_item_value,
    sum(freight_value) as total_freight_value,
    sum(price + freight_value) as total_order_value
from {{ ref('stg_order_items') }}
group by order_id