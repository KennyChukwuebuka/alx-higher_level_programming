#!/usr/bin/node
// Write a script that prints all characters of a Star Wars movie
// The first argument is the Movie ID - example: 3 = “Return of the Jedi”
// Display one character name by line in the same order of the list “characters” in the /films/ response
// You must use the Star wars API https://swapi-api.alx-tools.com/api/
// You must use the module request

const request = require('request');

const url = 'https://swapi.co/api/films/' + process.argv[2];
request(url, function (error, response, body) {
  if (!error) {
    const characters = JSON.parse(body).characters;
    characters.forEach((character) => {
      request(character, function (error, response, body) {
        if (!error) {
          console.log(JSON.parse(body).name);
        }
      });
    });
  }
});
