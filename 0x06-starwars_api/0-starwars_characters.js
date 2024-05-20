#!/usr/bin/node
const request = require('request');

const API_URL = 'https://swapi-api.hbtn.io/api';

if (process.argv.length > 2) {
  const movieId = process.argv[2];
  const filmUrl = `${API_URL}/films/${movieId}/`;

  request(filmUrl, (err, _, body) => {
    if (err) {
      console.log(err);
      process.exit(1);
    }

    const charactersUrls = JSON.parse(body).characters;
    const charactersNames = [];

    charactersUrls.forEach((characterUrl) => {
      request(characterUrl, (error, __, charactersReqBody) => {
        if (error) {
          console.log(`Error fetching character data: ${error}`);
          process.exit(1);
        }

        const characterName = JSON.parse(charactersReqBody).name;
        charactersNames.push(characterName);

        if (charactersNames.length === charactersUrls.length) {
          console.log(charactersNames.join('\n'));
        }
      });
    });
  });
}
