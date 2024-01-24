# Write your MySQL query statement below
select max(num) as num 
from (select num, count(num) as num_count 
from MyNumbers
group by num
having num_count = 1 order by num desc) new;