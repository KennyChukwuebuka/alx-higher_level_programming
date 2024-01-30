#!/usr/bin/node
// Write a script that prints all characters of a Star Wars movie:
// The first argument is the Movie ID - example: 3 = “Return of the Jedi”
// Display one character name by line
// You must use the Star wars API https://swapi-api.alx-tools.com/api/
// You must use the module request

const request = require('request');

request(`https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    console.log(JSON.parse(body).characters);
  }
});