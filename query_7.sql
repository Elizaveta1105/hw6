
SELECT s.fullname, AVG(n.note) as average_grade, g."name" as group_name
from notes n 
join students s on n.student_id = s.id
join subjects s2 on n.subject_id = s2.id
join "groups" g on s.group_id = g.id 
where g.id = 1 and s2.name = 'harness integrated deliverables'
group by s.fullname , g."name"