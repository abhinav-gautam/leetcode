-- https://leetcode.com/problems/biggest-single-number/description/?envType=study-plan-v2&envId=top-sql-50
select
    max(num) as num
from
    MyNumbers
where
    (num) in (
        select
            num
        from
            MyNumbers
        group by
            num
        having
            count(*) = 1
    );