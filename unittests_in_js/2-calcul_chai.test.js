const { expect } = require('chai');
const calculateNumber = require('./2-calcul_chai.js'); // Update the path to the new file

describe('calculateNumber', function () {
  it('should round and sum two numbers', function () {
    expect(calculateNumber('SUM', 1, 3)).to.equal(4);
  });

  it('should round and subtract two numbers', function () {
    expect(calculateNumber('SUBTRACT', 3, 1)).to.equal(2);
  });

  it('should round and divide two numbers', function () {
    expect(calculateNumber('DIVIDE', 4, 2)).to.equal(2);
  });
});

