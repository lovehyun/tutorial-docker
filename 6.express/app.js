const express = require('express');
const nunjucks = require('nunjucks');
const morgan = require('morgan');
require('dotenv').config();

const color = process.env.APP_COLOR;
const app = express();
const port = process.env.PORT || 3000;

nunjucks.configure('views', {
    autoescape: true,
    express: app,
});

// View Engine 설정
app.set('view engine', 'html');

// Morgan 설정
morgan.token('remote-addr', (req) => {
    // x-forwarded-for 헤더가 있는 경우 그 값을 사용하고, 없으면 기본 값인 req.ip를 사용
    return req.headers['x-forwarded-for'] || req.ip || '-';
});

app.use(morgan('combined'));

app.get('/', (req, res) => {
    res.render('hello.html', { color });
});

app.listen(port, () => {
    console.log(`Server is running on http://localhost:${port}`);
});
