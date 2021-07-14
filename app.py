from flask import Flask, jsonify
import json

app = Flask(__name__)


@app.route('/')
def hello():
    with open('config/conf.json', 'rb') as f:
        config = json.load(f)
        f.close()
    return jsonify({
        'body': config
    })

if __name__ == "__main__":
    app.debug = True
    app.run()
    app.run(host='0.0.0.0', port=5000)

