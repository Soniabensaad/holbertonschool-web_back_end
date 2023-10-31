-- 4. Buy buy buy
CREATE TRIGGER DecreaseItemQuantityAfterOrder
AFTER INSERT ON orders 
FOR EACH ROW
UPDATE items
SET stock_quantity = stock_quantity - NEW.number
WHERE name = NEW.item_id;
   
