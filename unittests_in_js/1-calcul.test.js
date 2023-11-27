const assert = require('assert');
const calculateNumber = require('./1-calcul.js');

describe('calculateNumber', function () {
  it('should round and sum two numbers', function () {
    assert.strictEqual(calculateNumber('SUM', 1, 3), 4);
  });

  it('should round and subtract two numbers', function () {
    assert.strictEqual(calculateNumber('SUBTRACT', 3, 1), 2);
  });

  it('should round and divide two numbers', function () {
    assert.strictEqual(calculateNumber('DIVIDE', 4, 2), 2);
  });
});
