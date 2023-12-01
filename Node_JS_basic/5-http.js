const http = require('http');
const countStudents = require('./3-read_file_async');

const args = process.argv.slice(2);
const DATABASE = args[0];

const hostname = '127.0.0.1';
const port = 1245;

const app = http.createServer(async (req, res) => {
  res.statusCode = 200;
  res.setHeader('Content-Type', 'text/plain');

  const { url } = req;

  if (url === '/') {
    res.write('Hello Holberton School!');
  } else if (url === '/students') {
    try {
      const students = await countStudents(DATABASE);
      res.write('This is the list of our students\n');

      // Display the number of students
      res.write(`Number of students: ${students.length}\n`);

      // Display the number of students in CS
      const csStudents = students.filter(student => student.field === 'CS');
      res.write(`Number of students in CS: ${csStudents.length}. List: ${csStudents.map(student => student.firstname).join(', ')}\n`);

      
      
      const sweStudents = students.filter(student => student.field === 'SWE');
      res.end(`Number of students in SWE: ${sweStudents.length}. List: ${sweStudents.map(student => student.firstname).join(', ')}`);
    } catch (error) {
      res.end(error.message);
    }
    return; 
  }

 
  res.statusCode = 404;
  res.end();
});

app.listen(port, hostname, () => {
  console.log(`Server running at http://${hostname}:${port}/`);
});

module.exports = app;
