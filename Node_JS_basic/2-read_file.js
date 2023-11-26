const fs = require('fs');

// Define the countStudents function
const countStudents = (filePath) => {
    try {
        return readDatabaseSync(filePath);
    } catch (error) {
        console.error(error.message);
        // Handle the error appropriately
    }
};

const readDatabaseSync = (filePath) => {
    try {
        // Read the file synchronously
        const data = fs.readFileSync(filePath, 'utf8');
        console.log('File content:', data);

        // Parse the data (replace this with your actual parsing logic)
        const parsedData = JSON.parse(data); // Assuming the data is in JSON format

        // Log the number of students for each field
        const fields = Object.keys(parsedData.students[0]); // Assuming all students have the same fields

        fields.forEach((field) => {
            const numberOfStudents = parsedData.students.filter((student) => student[field]).length;
            console.log(`Number of students in ${field}: ${numberOfStudents}`);
        });

        // Process the data or return it as needed
        return parsedData;
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
