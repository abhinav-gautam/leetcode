-- https://leetcode.com/problems/queries-quality-and-percentage/description/?envType=study-plan-v2&envId=top-sql-50
select
    query_name,
    round(avg(rating / position), 2) as quality,
    round(
        sum(
            case
                when rating < 3 then 1
                else 0
            end
        ) * 100 / count(*),
        2
    ) as poor_query_percentage
from
    queries
group by
    query_name;