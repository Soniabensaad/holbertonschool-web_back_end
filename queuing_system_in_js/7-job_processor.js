import kue from 'kue';
import redis from 'redis';

const blacklistedNumbers = ['4153518780', '4153518781'];

const queue = kue.createQueue({
  redis: {
    createClientFactory: function () {
      return redis.createClient();
    },
  },
});

function sendNotification(phoneNumber, message, job, done) {
  job.progress(0);

  if (blacklistedNumbers.includes(phoneNumber)) {
    return done(new Error(`Phone number ${phoneNumber} is blacklisted`));
  }

  job.progress(50);
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
  done();
}

// Process the jobs from the queue
queue.process('push_notification_code_2', 2, (job, done) => {
  sendNotification(job.data.phoneNumber, job.data.message, job, done);
});

// Create sample jobs
const phoneNumbers = [
  '4153518743',
  '4153538781',
  '4153118782',
  '4153718781',
  '4159518782',
  '4158718781',
  '4153818782',
  '4154318781',
  '4151218782',
];

phoneNumbers.forEach((phoneNumber, index) => {
  const message = `This is the code ${index % 2 === 0 ? '4321' : '4562'} to verify your account`;

  const notificationJob = queue.create('push_notification_code_2', {
    phoneNumber,
    message,
  });

  notificationJob
    .on('complete', () => {
      console.log(`Notification job #${notificationJob.id} completed`);
    })
    .on('failed', (err) => {
      console.log(`Notification job #${notificationJob.id} failed: ${err.message}`);
    })
    .save();
});

// Listen to queue events
queue.on('job enqueue', function (id, type) {
  console.log(`Notification job #${id} 0% complete`);
});

// Start the queue processing
queue.process('push_notification_code_2', 2, (job, done) => {
  sendNotification(job.data.phoneNumber, job.data.message, job, done);
});

console.log('Job processor is running...');
