-- 7. Average score
SELECT user_id, AVG(score) AS average_score
FROM user_scores
WHERE user_id = <user_id>
GROUP BY user_id;
