#!/usr/bin/node
const request = require('request');

const API_URL = 'https://swapi-api.hbtn.io/api';

if (process.argv.length > 2) {
  const movieId = process.argv[2];
  const filmURL = `${API_URL}/films/${movieId}/`;

  request(filmURL, (err, _, body) => {
    if (err) {
      console.log(err);
      process.exit(1);
    }

    const charactersURL = JSON.parse(body).characters;
    const charactersNames = [];

    charactersURL.forEach((characterURL) => {
      request(characterURL, (promiseErr, __, charactersReqBody) => {
        if (promiseErr) {
          console.log(promiseErr);
          process.exit(1);
        }

        const characterData = JSON.parse(charactersReqBody);
        const characterName = characterData.name;
        charactersNames.push(characterName);

        if (charactersNames.length === charactersURL.length) {
          console.log(charactersNames.join('\n'));
        }
      });
    });
  });
}
