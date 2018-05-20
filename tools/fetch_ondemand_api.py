from flask import Flask
import json

from fetch import multi_fetch

app = Flask(__name__)

@app.route('/api/currencies', methods=['GET'])
def get_currencies():
    result = multi_fetch()
    
    return json.dumps(result)


if __name__ == '__main__':
    app.run(debug=True)