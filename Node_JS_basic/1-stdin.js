console.log('Welcome to Holberton School, what is your name?\n');

const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

// Prompt the user for their name
rl.question('', (name) => {
  // Display the message with the entered name on a new line
  console.log(`Your name is: ${name}\n`);

  // Close the readline interface
  rl.close();

  // Display the closing message
  console.log('This important software is now closing\n');
});
