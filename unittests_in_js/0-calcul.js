module.exports = function calculateNumber (a, b=0) {
    let roundedA = Number(a);
    let roundedB = Number(b);
    let sum = Math.round(roundedA) + Math.round(roundedB);
    return sum;
}
