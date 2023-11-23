const cleanSet = (set, startString) => {
    const resultArray = [];
  
    set.forEach((value) => {
      if (typeof value === "string") {
        const stringValue = String(value); // Convert non-string values to string
        if (stringValue.startsWith(startString)) {
          const restOfString = stringValue.slice(startString.length);
          resultArray.push(restOfString);
        }
      }
    });
  
    if (resultArray.length === 0) {
      return "";
    }
  
    return resultArray.join("-");
  };
  
  export default cleanSet;
  