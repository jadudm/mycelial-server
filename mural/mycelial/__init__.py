from flask import Flask

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = '/Users/mjadud/git/mycelial/uploads'

import mycelial.views

if __name__ == "__main__":
    app.run(host='0.0.0.0', port = 4000, debug = True)
    