#!/usr/bin/node
const request = require('request');

const API_URL = 'https://swapi-api.hbtn.io/api';

if (process.argv.length > 2) {
  const movieId = process.argv[2];
  const filmUrl = `${API_URL}/films/${movieId}/`;

  request(filmUrl, (error, response, body) => {
    if (error) {
      console.log(error);
      process.exit(1);
    }

    if (response.statusCode === 200) {
      const charactersUrls = JSON.parse(body).characters;
      const charactersNames = [];

      charactersUrls.forEach((characterUrl) => {
        request(characterUrl, (characterError, characterResponse, characterBody) => {
          if (characterError) {
            console.log(`Error fetching character data: ${characterError}`);
            process.exit(1);
          }

          if (characterResponse.statusCode === 200) {
            const characterName = JSON.parse(characterBody).name;
            charactersNames.push(characterName);
          } else {
            console.log(`Error fetching character data: ${characterResponse.statusCode}`);
            process.exit(1);
          }

          // Check if all characters have been fetched
          if (charactersNames.length === charactersUrls.length) {
            console.log(charactersNames.join('\n'));
          }
        });
      });
    } else {
      console.log(`Error fetching movie data: ${response.statusCode}`);
      process.exit(1);
    }
  });
}
