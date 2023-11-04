--10. Safe divide
-- Create the SafeDiv function
-- Create the SafeDiv function
DELIMITER //
CREATE FUNCTION SafeDiv(a DECIMAL, b DECIMAL)
RETURNS DECIMAL
BEGIN
  DECLARE result DECIMAL;

  IF b = 0 THEN
    SET result = 0;
  ELSE
    SET result = a / b;
  END IF;

  RETURN result;
END;
//
DELIMITER ;
