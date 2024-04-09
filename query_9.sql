SELECT s.fullname as student_name, s2.name as subject_name
FROM subjects s2
LEFT JOIN notes n ON s2.id = n.subject_id
LEFT JOIN students s ON n.student_id = s.id
GROUP BY s.fullname, s2.name
ORDER BY s.fullname ASC