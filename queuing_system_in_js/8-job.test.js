import kue from 'kue';
import { expect } from 'chai';
import createPushNotificationsJobs from './8-job';

const queue = kue.createQueue();

const jobs = [
  {
    phoneNumber: '4153518780',
    message: 'This is the code 1234 to verify your account',
  },
];

describe('createPushNotificationsJobs', () => {
  before(() => {
    queue.testMode.enter();
  });

  afterEach(() => {
    queue.testMode.clear();
  });

  after(() => {
    queue.testMode.exit();
  });

  it('throws an error if jobs is not an array (Number)', () => {
    expect(() => {
      createPushNotificationsJobs(2, queue);
    }).to.throw(/Jobs is not an array/);
  });

  it('throws an error if jobs is not an array (Object)', () => {
    expect(() => {
      createPushNotificationsJobs({}, queue);
    }).to.throw(/Jobs is not an array/);
  });

  it('throws an error if jobs is not an array (String)', () => {
    expect(() => {
      createPushNotificationsJobs('Hello', queue);
    }).to.throw(/Jobs is not an array/);
  });

  it('does not throw an error if jobs is an empty array', () => {
    const ret = createPushNotificationsJobs([], queue);
    expect(ret).to.equal(undefined);
  });

  it('adds two jobs to the queue with the correct types and data', () => {
    queue.createJob('myJob', { foo: 'bar' }).save();
    queue.createJob('anotherJob', { baz: 'bip' }).save();

    expect(queue.testMode.jobs.length).to.equal(2);
    expect(queue.testMode.jobs[0].type).to.equal('myJob');
    expect(queue.testMode.jobs[0].data).to.eql({ foo: 'bar' });
    expect(queue.testMode.jobs[1].type).to.equal('anotherJob');
    expect(queue.testMode.jobs[1].data).to.eql({ baz: 'bip' });
  });

  
});
