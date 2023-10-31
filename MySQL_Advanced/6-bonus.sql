-- 6. Add bonus
CREATE PROCEDURE AddBonus(IN users INT, IN projects TEXT)
BEGIN
    INSERT INTO score (user_id, project_name)
    VALUES (studentId, correctionText);
END;
