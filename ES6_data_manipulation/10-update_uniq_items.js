const updateUniqueItems = (groceryMap) => {
    if (!(groceryMap instanceof Map)) {
      throw new Error('Cannot process');
    }
  
    groceryMap.forEach((quantity, item) => {
      if (quantity === 1) {
        groceryMap.set(item, 100);
      }
    });
  };
  
  export default updateUniqueItems;
  