CREATE TRIGGER ResetEmailOnUpdate
BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
    IF NEW.email != OLD.email THEN
        SET NEW.email = 'noemail@example.com';
    END IF;
END;
