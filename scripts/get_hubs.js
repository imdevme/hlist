#!/usr/local/bin/node

const $ = require('jquery');

const https = require('https');

const jsdom = require("jsdom");

const { JSDOM } = jsdom;

process.env.NODE_TLS_REJECT_UNAUTHORIZED = "0";

const urlHabr = 'https://habrahabr.ru/hubs/';

const dom = new JSDOM(``, {
  url: urlHabr,
  referrer: "https://habrahabr.ru/",
  contentType: "text/html",
});

console.log(dom.window.document.body.children);

// https.get(url, (res) => {

//   console.log('statusCode:', res.statusCode);
//   console.log('headers:', res.headers);

//   res.on('data', (d) => {
//     process.stdout.write(d);
//   });

// }).on('error', (e) => {
//   console.error(e);
// });