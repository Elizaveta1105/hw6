
SELECT s.fullname, n.note, g."name" as group_name, n.note_date
FROM notes n 
JOIN students s ON n.student_id = s.id
JOIN subjects s2 ON n.subject_id = s2.id
JOIN "groups" g ON s.group_id = g.id 
WHERE g.id = 1 AND s2.name = 'harness integrated deliverables'
AND (s.id, s2.id, n.note_date) IN (
    SELECT n.student_id, n.subject_id, MAX(n.note_date)
    FROM notes n
    JOIN subjects s2 ON n.subject_id = s2.id
    JOIN "groups" g ON s2.teacher_id = g.id 
    WHERE g.id = 1 AND s2.name = 'harness integrated deliverables'
    GROUP BY n.student_id, n.subject_id
)
