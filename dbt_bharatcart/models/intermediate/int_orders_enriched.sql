select
    o.order_id,
    o.customer_id,
    c.customer_unique_id,
    c.customer_city,
    c.customer_state,
    o.order_status,
    o.order_purchase_timestamp,
    o.order_approved_at,
    o.order_delivered_carrier_date,
    o.order_delivered_customer_date,
    o.order_estimated_delivery_date,

    coalesce(i.item_count, 0) as item_count,
    coalesce(i.distinct_product_count, 0) as distinct_product_count,
    coalesce(i.seller_count, 0) as seller_count,
    coalesce(i.total_item_value, 0) as total_item_value,
    coalesce(i.total_freight_value, 0) as total_freight_value,
    coalesce(i.total_order_value, 0) as total_order_value,

    coalesce(p.payment_record_count, 0) as payment_record_count,
    coalesce(p.total_payment_value, 0) as total_payment_value,
    coalesce(p.max_payment_installments, 0) as max_payment_installments,

    coalesce(r.review_count, 0) as review_count,
    r.avg_review_score,
    r.max_review_score,
    r.min_review_score,

    datediff(
        'day',
        o.order_purchase_timestamp,
        o.order_delivered_customer_date
    ) as delivery_days,

    datediff(
        'day',
        o.order_estimated_delivery_date,
        o.order_delivered_customer_date
    ) as days_vs_estimate,

    case
        when o.order_delivered_customer_date is null then null
        when o.order_delivered_customer_date
            <= o.order_estimated_delivery_date then true
        else false
    end as delivered_on_time

from {{ ref('stg_orders') }} as o

left join {{ ref('stg_customers') }} as c
    on o.customer_id = c.customer_id

left join {{ ref('int_order_items_agg') }} as i
    on o.order_id = i.order_id

left join {{ ref('int_order_payments_agg') }} as p
    on o.order_id = p.order_id

left join {{ ref('int_order_reviews_agg') }} as r
    on o.order_id = r.order_id