#!/usr/bin/node

const fs = require('fs');
const filePath = process.argv[2]; // Get the file path from command line arguments

fs.readFile(filePath, 'utf-8', (err, data) => {
	if (err) {
		console.error(err); // Print the error object if an error occurred during reading
	 } else {
		console.log(data); // Print the content of the file
		}
	 });
