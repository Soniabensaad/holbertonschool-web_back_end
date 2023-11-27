function calculateNumber (a, b) {
    let roundedA = Math.round(a);
    let roundedB = Math.round(b);
    let sum = roundedA + roundedB;
    return sum;
}
module.exports = calculateNumber;
