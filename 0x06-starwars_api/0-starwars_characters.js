#!/usr/bin/node
/**
 * a script that prints all characters of star wars movie
 */
const args = require('process').argv
const request = require('request')


const fetchApi = (id) => {
  const url = `https://swapi-api.alx-tools.com/api/films/${id}`;

  return new Promise((resolve, reject) => {
    request(url)
      .then(response => {
        return response.json();
      })
      .then(filmData => {
        const characterURLs = filmData.characters;
        const characterNamesPromises = characterURLs.map(characterURL => {
          return fetch(characterURL)
            .then(response => {
              if (!response.ok) {
                throw new Error('Failed to fetch character');
              }
              return response.json();
            })
            .then(characterData => characterData.name);
        });

        return Promise.all(characterNamesPromises);
      })
      .then(characterNames => {
        characterNames.forEach(characterName => console.log(characterName));
        resolve();
      })
      .catch(error => {
        console.error('Error:', error);
        reject(error);
      });
  });
};


fetchApi(args[2]);
