-- https://leetcode.com/problems/students-and-examinations/description/?envType=study-plan-v2&envId=top-sql-50

select st.student_id, st.student_name, su.subject_name, count(e.student_id) as attended_exams
from students st 
cross join subjects su 
left join examinations e 
on st.student_id = e.student_id and su.subject_name = e.subject_name
group by st.student_id, su.subject_name
order by st.student_id asc, su.subject_name asc;