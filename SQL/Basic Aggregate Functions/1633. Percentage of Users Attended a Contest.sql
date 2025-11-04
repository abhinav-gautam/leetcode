-- https://leetcode.com/problems/percentage-of-users-attended-a-contest/description/?envType=study-plan-v2&envId=top-sql-50
select
    contest_id,
    round(
        count(*) * 100 /(
            select
                count(*)
            from
                users
        ),
        2
    ) as percentage
from
    register
group by
    contest_id
order by
    percentage desc,
    contest_id asc;