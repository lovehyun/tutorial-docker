const express = require('express');
const app = express();

const os = require('os');
const port = 3000;

app.get('/', function (req,res) {
    // res.send('Hello Express\n');

    // ip = req.connection.remoteAddress; // 예전 방식, express4 부터는 req.ip 로 단축
    ip = req.ip;
    // ip = req.headers['x-forwarded-for'] || req.ip;

    console.log(`Received request from ${ip}`);
    res.send(`<h2>Welcome to ${os.hostname()} </h2>\n`);
    // res.send(`<h1>Welcome to ${os.hostname()} </h1>\n`);
});

app.listen(port, () => {
    console.log(`Express is ready at http://localhost:${port}`);
    // console.log(`Express is ready at http://${os.hostname}:${port}`);
});
