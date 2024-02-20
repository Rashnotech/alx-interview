#!/usr/bin/node
/**
 * a script that prints all characters of star wars movie
 */
const args = require('process').argv
const request = require('request')

const id = args[2]
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;

const fetchApi = (id) => {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (response.statusCode === 200) {
        const characters = JSON.parse(body).characters;
	resolve(characters)
      } else {
        reject(response);
      }
    })
  }
}

request(url, (error, response, body) => {
  const characters = JSON.parse(body).characters;
  const promises = characters.map(character => fetchApi(character));
  Promise.all(promises)
  .then(results = results.forEach(result, console.log(result))
  .catch(error => console.log(error));
});
