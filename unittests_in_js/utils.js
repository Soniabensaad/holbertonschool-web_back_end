// utils.js
function isNegZero(n) {
    n = Number(n);
    return n === 0 && 1 / n === -Infinity;
  }
  
  function calculateNumber(type, a, b) {
    const roundedA = Math.round(a);
    const roundedB = Math.round(b);
  
    switch (type) {
      case 'SUM':
        return roundedA + roundedB;
      case 'SUBTRACT':
        return roundedA - roundedB;
      case 'DIVIDE':
        if (roundedB === 0) {
          throw new Error('Cannot divide by zero');
        }
        const quotient = roundedA / roundedB;
        return isNegZero(quotient) ? 0 : quotient;
  
      default:
        throw new Error('Invalid operation type');
    }
  }
  
  module.exports = { calculateNumber };
  