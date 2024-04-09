SELECT t.fullname as teacher_name, s."name" as subject_name, AVG(n.note) as average_grade
FROM teachers t
LEFT JOIN subjects s ON t.id = s.teacher_id
LEFT JOIN notes n ON s.id = n.subject_id
GROUP BY s."name", t.fullname
