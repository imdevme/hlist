var assert = require('assert');
var express = require('express');
var mongoose = require('mongoose');
var bodyParser = require('body-parser');

var urlMongo = 'mongodb://localhost:27017/test';

mongoose.connect(urlMongo);

var articleSchema = mongoose.Schema({
    title : String,
    link  : String,
    datePublish : Date,
    rating : Number

});

var Article = mongoose.model('Article', articleSchema);

var app = express();

app.use( bodyParser.json() );
app.use(express.static('frontend/src'));
app.use(express.static('data/json'));

app.get('/api/v1/articles', function(request, response){

    Article.find({}, function(error, articles){
        if (error) {
            response.status(500).send(error);
        } else {
            response.json({articles: articles});
        }
    });

});

app.post('/api/v1/articles', function(request, response) {

    var article = new Article({
        title : request.body.title,
        link  : request.body.link,
        datePublish : request.body.datePublish,
        rating : request.body.rating
    });

    article.save().then(function(e){
        console.log(e);
        response.json({isSuccess: true});
    });

});


const port = 3500;

app.listen(port, function(){
    console.log('Start node server on port ' + port);
});