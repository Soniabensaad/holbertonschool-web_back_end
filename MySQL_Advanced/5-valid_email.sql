-- 5. Email validation to sent
CREATE TRIGGER valid_email
BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
    IF NEW.email != OLD.email THEN
        SET NEW.email = 'noemail@example.com';
    END IF;
END;
