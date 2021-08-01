import os
from flask import Flask, render_template

app = Flask(__name__)

color = os.environ.get('APP_COLOR')

@app.route('/')
def main():
    return render_template('hello.html', color=color)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
