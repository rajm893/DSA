# Write your MySQL query statement below
with ct as(
    select student_id, student_name, subject_name
    from Students cross join Subjects)

select s.student_id, s.student_name, s.subject_name, 
sum(case when e.subject_name is null then 0 else 1 end ) as attended_exams 
from ct s left join Examinations e
on s.student_id = e.student_id and s.subject_name = e.subject_name
group by s.student_id, s.student_name, s.subject_name 
order by s.student_id, s.student_name, s.subject_name 
