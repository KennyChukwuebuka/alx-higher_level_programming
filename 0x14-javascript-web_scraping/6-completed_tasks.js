#!/usr/bin/node
// Write a script that computes the number of tasks completed by user id.
// The first argument is the API URL: https://jsonplaceholder.typicode.com/todos
// Only print users with completed task
// You must use the module request

const request = require('request');

request('https://jsonplaceholder.typicode.com/todos', (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const completedTasks = JSON.parse(body).filter((task) => task.completed === true);
    console.log(completedTasks.length);
  }
});
