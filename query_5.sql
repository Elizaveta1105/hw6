SELECT t.fullname, MIN(s."name") AS subject_name
FROM teachers t
join subjects s on s.teacher_id = t.id 
group by t.fullname