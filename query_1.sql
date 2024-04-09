
select s.id, s.fullname, ROUND(AVG(n.note), 2) as average_note
from students s
join notes n on s.id = n.student_id 
group by s.id
order by average_note DESC
limit 5