#!/usr/bin/node
// Write a script that prints the number of movies where the character “Wedge Antilles” is present
// The first argument is the API URL of the Star wars API: https://swapi-api.alx-tools.com/api/films/
// Wedge Antilles is character ID 18 - your script must use this ID for filtering the result of the API
// You must use the module request

const request = require('request');

request('https://swapi-api.alx-tools.com/api/films/?format=json', (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    console.log(JSON.parse(body).count);
  }
});
