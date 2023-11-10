export default function appendToEachArrayValue(array, appendString) {
  const p = [];
  for (const value of array) {
    p.push(appendString + value);
  }
  return p;
}
