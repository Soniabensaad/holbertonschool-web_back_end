// 1-stdin.js

cprocess.stdout.write('Welcome to Holberton School, what is your name?\n');

process.stdin.setEncoding('utf8');

process.stdin.on('readable', () => {
  const line = process.stdin.read();
  if (line !== null) {
    process.stdout.write(`Your name is: ${line}`);
  }
});

process.stdin.on('end', () => {
  process.stdout.write('This important software is now closing\n');
});
