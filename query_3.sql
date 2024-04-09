SELECT g."name" AS group_name, ROUND(AVG(n.note), 2) AS average_note
FROM notes n
JOIN students s ON n.student_id = s.id 
JOIN "groups" g ON s.group_id = g.id
GROUP BY g."name"
ORDER BY average_note DESC;
