# Write your MySQL query statement below
with combine as(
select s.user_id, c.action
from Signups s left join Confirmations c
on s.user_id = c.user_id)

select user_id,
round(sum(case when action = "confirmed" then 1 else 0 end)/count(*),2) as confirmation_rate
from combine
group by user_id

