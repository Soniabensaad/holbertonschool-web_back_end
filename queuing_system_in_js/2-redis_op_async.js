import redis from 'redis';
import { promisify } from 'util';
import fs from 'fs';

const client = redis.createClient();
const readFileAsync = promisify(fs.readFile);

client.on('error', (error) => {
  console.log(`Redis client not connected to the server: ${error.message}`);
});

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

function setNewSchool(schoolName, value) {
  client.set(schoolName, value, redis.print);
}

async function displaySchoolValue(schoolName) {
  try {
    const getAsync = promisify(client.get).bind(client);
    const data = await getAsync(schoolName);
    console.log(`Value of '${schoolName}': ${data}`);
  } catch (error) {
    console.error(`Error getting key '${schoolName}': ${error.message}`);
    client.quit();
  }
}
displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
