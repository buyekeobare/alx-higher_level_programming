#!/usr/bin/node
// print all characters of a Star Wars movie synchronously
const request = require('request');

// Gets movie ID from command line argument
const movieId = process.argv[2];

// Constructs URL to fetch movie data
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

// Makes a request to fetch movie data
request(url, (error, response, body) => {
  // Handles errors
  if (error) {
    console.error('Error:', error);
    return;
  }

  // Parses movie data
  const film = JSON.parse(body);

  // Gets URLs of characters in the movie
  const charactersUrls = film.characters;

  // Creates an array of promises that will fetch the data of each character
  const charactersPromises = charactersUrls.map(characterUrl => {
    // Creates a promise that will fetch the data of a character
    return new Promise((resolve, reject) => {
      // Makes a request to fetch character data
      request(characterUrl, (error, response, body) => {
        // Handles errors
        if (error) {
          reject(error);
          return;
        }

        // Parses character data
        const character = JSON.parse(body);

        // Resolvse the promise with the name of the character
        resolve(character.name);
      });
    });
  });

  // Waits for all promises to resolve and thens print the names of the characters
  Promise.all(charactersPromises)
    .then(characters => {
      console.log(characters.join('\n'));
    })
    .catch(error => {
      console.error('Error:', error);
    });
});
