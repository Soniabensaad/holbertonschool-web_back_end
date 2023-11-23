const groceriesList = () => {
    const items = [
      { name: 'Apples', quantity: 10 },
      { name: 'Tomatoes', quantity: 10 },
      { name: 'Pasta', quantity: 1 },
      { name: 'Rice', quantity: 1 },
      { name: 'Banana', quantity: 5 },
    ];
  
    const groceryMap = new Map();
  
    items.forEach(({ name, quantity }) => {
      groceryMap.set(name, quantity);
    });
  
    return groceryMap;
  };
  
  export default groceriesList;
  