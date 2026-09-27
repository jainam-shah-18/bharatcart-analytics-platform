select
    order_id,
    payment_sequential,
    lower(trim(payment_type)) as payment_type,
    payment_installments,
    payment_value
from {{ source('raw', 'olist_order_payments') }}