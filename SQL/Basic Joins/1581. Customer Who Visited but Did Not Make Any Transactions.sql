-- https://leetcode.com/problems/customer-who-visited-but-did-not-make-any-transactions/description/?envType=study-plan-v2&envId=top-sql-50

select customer_id, count(*) as count_no_trans 
from Visits left join Transactions using(visit_id) 
where transaction_id is null 
group by 1;