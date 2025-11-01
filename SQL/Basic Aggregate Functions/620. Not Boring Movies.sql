-- https://leetcode.com/problems/not-boring-movies/?envType=study-plan-v2&envId=top-sql-50

select * from Cinema 
where description != 'boring' and id % 2 = 1 
order by rating desc;