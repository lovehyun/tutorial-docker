var express = require('express');
var app = express();

var os = require('os');


app.get('/', function (req,res) {
    // res.send('Hello Express\n');

    ip = req.connection.remoteAddress;
    // ip = req.headers['x-forwarded-for'] || req.connection.remoteAddress;

    console.log('Received request from ' + ip);
    res.send('<h2>Welcome to ' + os.hostname() + '</h2>\n');
    // res.send('<h1>Welcome to ' + os.hostname() + '</h1>\n');
});

app.listen(8000, () => 
    console.log('Express is ready at http://localhost:8000')
    // console.log('Express is ready at http://%s:8000', os.hostname())
);
