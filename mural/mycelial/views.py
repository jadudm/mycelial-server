from mycelial import app
from flask import request

import base64
import time
import uuid

ALLOWED_EXTENSIONS = set(['jpg', 'png'])

def get_extension(filename):
    return filename.rsplit('.', 1)[1]

def allowed_file(filename):
    return ('.' in filename 
            and 
            get_extension(filename) in ALLOWED_EXTENSIONS
            )
           
@app.route('/')
def index():
    return "Hello World!"

@app.route('/up/<name>', methods = ['GET', 'POST'])
def up(name):
    if request.method == 'GET':
        print("GET %s" % name)        
    elif request.method == 'POST':
        print("POST Uploading...")
        # print(request.files)
        print(request.url)
        imagedata = request.get_data(cache=False, as_text=True, parse_form_data=False)
        # The data comes in "websafe" from AppInventor's
        # bogo Base64 encoding.
        # + --> - (char 62, plus to dash)
        # / --> _ (char 63, slash to underscore)
        # = --> * padding
        for pair in [('-', '+'), ('_', '/'), ('*', '=')]:
            imagedata = imagedata.replace(pair[0], pair[1])
        missing_padding = len(imagedata) % 4
        if missing_padding != 0:
            imagedata += '='* (4 - missing_padding)
        print(imagedata)
        imagefp = open("/tmp/uploads/{0}.jpg".format(uuid.uuid4()), 'wb')
        imagefp.write(base64.b64decode(imagedata))
        imagefp.close()
        

        return "OK"
        
        # https://stackoverflow.com/questions/10434599/how-to-get-data-received-in-flask-request
        if file and allowed_file(name):
            filename = "{0}.{1}".format(str(uuid.uuid4()),  get_extension(name))
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('index'))
    else:
        print("R: {0}".format(request))
        print("Something failed.")
                
    return "Upload %s" % name
    
@app.route('/upload/<string:name>', methods = ['GET', 'POST'])
def upload(name):
    if request.method == 'GET':
        print("GET %s" % name)        
    elif request.method == 'POST':
        print("POST Uploading...")
        # print(request.files)
        print(request.url)
        # data = request.get_data(cache=False, as_text=False, parse_form_data=True)
        data = request.stream()
        print(data)
        
        # file = request.files['file']
        file = data
        if file and allowed_file(name):
            filename = "{0}.{1}".format(str(uuid.uuid4()),  get_extension(name))
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('index'))
    else:
        print("R: {0}".format(request))
        print("Something failed.")
                
    return "Upload %s" % name