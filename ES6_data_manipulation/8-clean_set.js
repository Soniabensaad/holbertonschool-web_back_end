const cleanSet = (set, startString) => {
    const resultArray = [];

    set.forEach((value) => {
        if (typeof value === "string" || resultArray.length === 0) {
            if (value.startsWith(startString)) {
                const restOfString = value.slice(startString.length);
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
