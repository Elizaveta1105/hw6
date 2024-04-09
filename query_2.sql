#Знайти середній бал у групах з певного предмета.

select s.group_id, ROUND(AVG(n.note), 2) as average_note, s2."name", groups.name  
from students s
join notes n on s.id = n.student_id 
join subjects s2 on n.subject_id = s2.id
group by s.group_id , s2."name" 
order by average_note DESC