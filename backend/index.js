var assert = require('assert');
var express = require('express');

var mongo = {
    db : null
};

var MongoClient = require('mongodb').MongoClient;

var urlMongo = 'mongodb://localhost:27017/test';


MongoClient.connect(urlMongo, function(error, db){
    assert.equal(null, error);
    console.log('Connected successfully to mongo');
    mongo.db = db;
});

// function insertDocs(db, callback) {
    
//     var collection = db.collection('documents');

//     collection.insertMany([
//         {a : 1},
//         {a : 2}
//     ], function (error, result) {
//         callback (result);
//     });

// }

// function findDocs(db, callback) {

//     var collection = db.collection('documents');

//     collection.find({}).toArray(function(error, docs){
//         console.log(docs);
//         callback(docs);
//     });

// }


var app = express();

app.use(express.static('frontend/src'));

app.get('/api/v1/articles', function(request, response){
    mongo.db.collection('articles').find({}).toArray(function(error, articles){
        if (error) {
            response.status(500).send(error);
        } else {
            response.json({articles: articles});
        }
    });
});

const port = 3500;

app.listen(port, function(){
    console.log('Start node server on port ' + port);
});