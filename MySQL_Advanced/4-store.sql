-- 4. Buy buy buy
CREATE TRIGGER DecreaseItemQuantityAfterOrder
AFTER INSERT ON orders 
FOR EACH ROW
-- Decrease the stock_quantity in the items table
UPDATE items
SET stock_quantity = stock_quantity - NEW.quantity
WHERE item_id = NEW.item_id;
   
