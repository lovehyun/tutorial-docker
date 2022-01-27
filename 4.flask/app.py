import os
from flask import Flask, render_template
from werkzeug.middleware.proxy_fix import ProxyFix

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app, x_proto=1, x_host=1)

color = os.environ.get('APP_COLOR')

@app.route('/')
def main():
    return render_template('hello.html', color=color)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
