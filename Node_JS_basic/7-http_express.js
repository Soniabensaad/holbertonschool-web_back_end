const express = require('express');
const countStudents = require('./3-read_file_async');

const app = express();
const port = 1245;

app.get('/', (req, res) => res.send('Hello Holberton School!'));

app.get('/students', async (req, res) => {
  res.setHeader('Content-Type', 'text/plain');
  const output = 'This is the list of our students\n';

  try {
    const students = await countStudents(process.argv[2]);

    // Display the number of students
    res.write(output);
    res.write(`Number of students: ${students.length}\n`);

    // Display the number of students in CS
    const csStudents = students.filter(student => student.field === 'CS');
    res.write(`Number of students in CS: ${csStudents.length}. List: ${csStudents.map(student => student.firstname).join(', ')}\n`);

    // Display the number of students in SWE
    const sweStudents = students.filter(student => student.field === 'SWE');
    res.end(`Number of students in SWE: ${sweStudents.length}. List: ${sweStudents.map(student => student.firstname).join(', ')}`);
  } catch (error) {
    // Handle the case where the database file doesn't exist
    res.end(output + error.message);
  }
});

app.listen(port, () => {
  console.log(`Server running at http://localhost:${port}/`);
});

module.exports = app;
