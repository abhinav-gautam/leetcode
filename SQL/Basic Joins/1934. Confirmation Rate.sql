-- https://leetcode.com/problems/confirmation-rate/description/?envType=study-plan-v2&envId=top-sql-50

select user_id, round(ifnull(avg(action='confirmed'),0),2) as confirmation_rate 
from Signups left join Confirmations 
using(user_id) 
group by user_id;