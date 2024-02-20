#!/usr/bin/node
/**
 * a script that prints all characters of a star wars movie
 */
const args = require('process').argv;
const request = require('request');

const id = args[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;

const fetchApi = (url) => {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error) console.log(error);
      if (response.statusCode === 200) {
        const characters = JSON.parse(body).name;
        resolve(characters);
      } else {
        reject(response);
      }
    });
  });
};

request(url, (error, response, body) => {
  if (error) console.log(error);
  const characters = JSON.parse(body).characters;
  const promise = characters.map(character => fetchApi(character));
  Promise.all(promise)
    .then(results => results.forEach(result => console.log(result)))
    .catch(error => console.log(error));
});
