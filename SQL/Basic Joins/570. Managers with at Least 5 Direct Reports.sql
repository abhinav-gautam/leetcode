-- https://leetcode.com/problems/managers-with-at-least-5-direct-reports/?envType=study-plan-v2&envId=top-sql-50

select e1.name
from employee e1 
join employee e2 on e1.id=e2.managerId
group by e2.managerId
having count(e2.managerId) >= 5
;