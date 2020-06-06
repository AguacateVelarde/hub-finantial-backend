#!flask/bin/python
import os
from flask import Flask
from services.belvo_connect import Belvo

app = Flask(__name__)


@app.route('/api')
def index():
    belvo = Belvo(os.getenv('BELVO_SECRET_ID'),
                  os.getenv('BOLVO_SECRET_PASSWORD'))

    return belvo.list_institutions()


@app.errorhandler(404)
def error_not_found(error):
    print(error)
    return {
        "message": "Not found error",
        "status_code": 404
    }


if __name__ == '__main__':
    app.run(debug=True)
