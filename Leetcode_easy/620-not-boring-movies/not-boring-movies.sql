# Write your MySQL query statement below

select *
from Cinema c
where description != 'boring' and id mod 2 = 1
order by rating desc