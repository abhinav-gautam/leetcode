-- https://leetcode.com/problems/average-time-of-process-per-machine/?envType=study-plan-v2&envId=top-sql-50

-- Write your MySQL query statement below
select a1.machine_id, round(avg(a2.timestamp - a1.timestamp), 3) as processing_time 
from Activity a1 join Activity a2 
on a1.machine_id = a2.machine_id 
and a1.process_id = a2.process_id
and a1.activity_type = 'start' 
and a2.activity_type = 'end'
where a1.activity_type ='start' and a2.activity_type ='end' 
group by machine_id;