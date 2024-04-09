SELECT t.fullname as teacher_name, s.fullname as student_name, s2.name as subject_name
FROM subjects s2
LEFT JOIN notes n ON s2.id = n.subject_id
LEFT JOIN students s ON n.student_id = s.id
LEFT JOIN teachers t ON s2.teacher_id = t.id
where s.fullname = 'Adam Park'
GROUP BY s.fullname, s2.name, t.fullname 

