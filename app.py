from flask import Flask, jsonify
import json
import os
import configparser
app = Flask(__name__)

path = 'config-vol/conf.json/conf.json'


with open(path, 'rb') as f:
  config = json.load(f)

@app.route('/')
def hello():
    print(config)
    return jsonify({
        'Hi':"Hello World!"
    })

if __name__ == "__main__":
  app.debug = True
  app.run()
  app.run(host='0.0.0.0', port=5000)


