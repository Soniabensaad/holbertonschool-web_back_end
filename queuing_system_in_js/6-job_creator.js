const kue = require('kue');

// Create a queue with Kue
const queue = kue.createQueue();

// Define a job type for push notifications
const pushNotificationJobType = 'push_notification_code';

// Sample job data
const jobData = {
  phoneNumber: '21622514123',
  message: 'This is a push notification!',
};

// Enqueue a job in the 'push_notification_code' queue
const pushNotificationJob = queue.create(pushNotificationJobType, jobData)
  .priority('high')
  .save((err) => {
    if (!err) {
      console.log(`Notification job created: JOB ID ${pushNotificationJob.id}`);
    } else {
      console.error('Notification job failed:', err);
    }
    // Close the queue connection when done
    queue.shutdown(5000, (err) => {
      console.log('Queue connection closed');
      process.exit(0);
    });
  });

// Event handler for job completion
pushNotificationJob.on('complete', () => {
  console.log('Notification job completed');
});

// Event handler for job failure
pushNotificationJob.on('failed', (err) => {
  console.error('Notification job failed:', err);
});

// Gracefully shut down the queue on process exit
process.on('SIGTERM', () => {
  queue.shutdown(5000, (err) => {
    console.log('Queue connection closed on process exit');
    process.exit(0);
  });
});
