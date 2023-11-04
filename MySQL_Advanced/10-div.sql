--10. Safe divide
-- Create the SafeDiv function
DELIMITER //
CREATE FUNCTION SafeDiv(a INT, b INT)
RETURNS INT
BEGIN
  DECLARE result INT;

  IF b = 0 THEN
    SET result = 0;
  ELSE
    SET result = a / b;
  END IF;

  RETURN result;
END;
//
DELIMITER ;
