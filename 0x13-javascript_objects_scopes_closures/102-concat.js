#!/usr/bin/node

const fs = require('fs');

function concatFiles (file1, file2, destination) {
  fs.readFile(file1, 'utf8', (err, data1) => {
    if (err) {
      console.error(`Error reading ${file1}: ${err}`);
      return;
    }

    fs.readFile(file2, 'utf8', (err, data2) => {
      if (err) {
        console.error(`Error reading ${file2}: ${err}`);
        return;
      }

      const concatenatedData = data1 + data2;

      fs.writeFile(destination, concatenatedData, (err) => {
        if (err) {
          console.error(`Error writing to ${destination}: ${err}`);
        }
      });
    });
  });
}

// Usage: node concatFiles.js file1.txt file2.txt destination.txt
const [,, file1, file2, destination] = process.argv;

concatFiles(file1, file2, destination);

/*
const fs = require('fs').promises;
const { argv } = require('process');

fs.readFile(argv[2], 'utf8')
  .then(data => fs.writeFile(argv[4], data, 'utf8'))
  .catch(err => console.error(err));

fs.readFile(argv[3], 'utf8')
  .then(data => fs.writeFile(argv[4], data, { flag: 'a' }, 'utf8'))
  .catch(err => console.error(err));
*/
