const redis = require('redis');

const redis_client = redis.createClient();

redis_client.hset('HolbertonSchools', 'Portland', '50', redis.print);
redis_client.hset('HolbertonSchools', 'Seattle', '80', redis.print);
redis_client.hset('HolbertonSchools', 'New York', '20', redis.print);
redis_client.hset('HolbertonSchools', 'Bogota', '20', redis.print);
redis_client.hset('HolbertonSchools', 'Cali', '40', redis.print);
redis_client.hset('HolbertonSchools', 'Paris', '2', redis.print);

redis_client.hgetall('HolbertonSchools', (err, value_data) => {
    if (err) {
        console.error('Error:', err);
    } else {
        console.log('Value Data:', value_data);

        for (const [field, value] of Object.entries(value_data)) {
            console.log(`${field}: ${value}`);
        }
    }
});
