import redis from 'redis';

const client = redis.createClient();
const channelName = 'holberton_school_channel';

client.on('error', (error) => {
  console.log(`Redis client not connected to the server: ERROR MESSAGE ${error.message}`);
});

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.subscribe(channelName);

client.on('message', (channel, message) => {
  console.log(`Received message from channel ${channel}: ${message}`);

  if (message === 'KILL_SERVER') {
    console.log('Received KILL_SERVER message. Unsubscribing and quitting.');
    client.unsubscribe(channelName);
    client.quit();
  }
});
