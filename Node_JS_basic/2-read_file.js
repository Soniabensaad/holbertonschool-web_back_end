const fs = require('fs');
const csv = require('csv-parser');

// Define the countStudents function
const countStudents = (filePath) => {
    try {
        const students = readDatabaseSync(filePath);
        const totalStudents = students.length;

        console.log(`Number of students: ${totalStudents}`);

        // Log the number of students for each field
        const fields = Object.keys(students[0]);

        fields.forEach((field) => {
            const studentsInField = students
                .filter((student) => student[field])
                .map((student) => student[field]);

            console.log(`Number of students in ${field}: ${studentsInField.length}. List: ${studentsInField.join(', ')}`);
        });
    } catch (error) {
        console.error(error.message);
        // Handle the error appropriately
    }
};

const readDatabaseSync = (filePath) => {
    const students = [];

    try {
        // Read the CSV file using csv-parser
        const fileStream = fs.createReadStream(filePath);
        fileStream
            .pipe(csv())
            .on('data', (row) => {
                // Assuming 'name' is one of the fields in your CSV
                if (row.name) {
                    students.push(row);
                }
            })
            .on('end', () => {
                // File reading is complete
            });

        return students;
    } catch (error) {
        console.error('Error reading file:', error.message);
        // If the error is due to the file not being found, throw a custom error
        if (error.code === 'ENOENT') {
            throw new Error('Cannot load the database. File not found.');
        }
        // Handle other errors appropriately
        throw error;
    }
};

module.exports = countStudents;
