// 4-payment.test.js
const { expect } = require('chai');
const sinon = require('sinon');
const { sendPaymentRequestToApi } = require('./4-payment');
const Utils = require('./utils');

describe('sendPaymentRequestToApi', function () {
  it('should use a stub to always return 10 and log the correct message', function () {
    const calculateNumberStub = sinon.stub(Utils, 'calculateNumber').returns(10);

    const consoleLogSpy = sinon.spy(console, 'log');

    // Call the function
    sendPaymentRequestToApi(100, 20);

    expect(calculateNumberStub.calledOnceWithExactly('SUM', 100, 20)).to.be.true;

    expect(consoleLogSpy.calledOnceWithExactly('The total is: 10')).to.be.true;

    calculateNumberStub.restore();
    consoleLogSpy.restore();
  });
});
