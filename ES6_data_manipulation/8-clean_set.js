const cleanSet = (set, startString) => {
    const resultArray = [];
  
    set.forEach((value) => {
      if (value.startsWith(startString)) {
        const restOfString = value.slice(startString.length);
        resultArray.push(restOfString);
      }
    });
  
    return resultArray.join("-");
  };
  
  export default cleanSet;
  