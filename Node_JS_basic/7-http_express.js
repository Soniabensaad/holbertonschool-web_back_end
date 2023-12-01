const express = require('express');
const countStudents = require('./3-read_file_async');

const app = express();
const port = 1245;

app.get('/', (req, res) => res.send('Hello Holberton School!'));

app.get('/students', async (req, res) => {
  res.writeHead(200, { 'Content-Type': 'text/plain' });
  const output = 'This is the list of our students\n';
  try {
    const students = await countStudents(process.argv[2]);
    res.end(`This is the list of our students\n${students.join('\n')}`);
  } catch (error) {
    res.end(output + error.message);
  }
});

app.listen(port);

module.exports = app;
