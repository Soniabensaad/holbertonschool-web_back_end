const http = require('http');

// Create an HTTP server
const server = http.createServer((req, res) => {
  // Set the response header
  res.writeHead(200, { 'Content-Type': 'text/plain' });

  // Send a response
  res.end('Hello Holberton School!');
});

// Specify the port and IP address for the server to listen on
const port = 1245;
const hostname = '127.0.0.1';

// Start the server and listen on the specified port and IP address
server.listen(port, hostname, () => {
  console.log(`Server running at http://${hostname}:${port}/`);
});
