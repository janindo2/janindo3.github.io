pip install flask
from flask import Flask

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def hello():
   message = "Hello, Flask!"
   return message

if __name__ == '__main__':
   app.run()
