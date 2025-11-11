-- https://leetcode.com/problems/customers-who-bought-all-products/description/?envType=study-plan-v2&envId=top-sql-50
select
    customer_id
from
    customer
group by
    customer_id
having
    count(distinct product_key) = (
        select
            count(*)
        from
            product
    );