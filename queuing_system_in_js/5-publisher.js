import redis from 'redis';

const client = redis.createClient();

client.on('error', (error) => {
    console.log(`Redis client not connected to the server: ERROR MESSAGE ${error.message}`);
});

client.on('connect', () => {
    console.log('Redis client connected to the server');
});

function publishMessage(message, delay) {
  setTimeout(() => {
      console.log(`About to send ${message}`);
      client.publish(channelName, message);
  }, delay);
}
const channelName = 'holberton school channel'; // Make sure to define `channelName`

publishMessage("Holberton Student #1 starts course", 100);
publishMessage("Holberton Student #2 starts course", 200);
publishMessage("KILL_SERVER", 300);
publishMessage("Holberton Student #3 starts course", 400);
