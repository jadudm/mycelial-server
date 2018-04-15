from mycelial import app

@app.route('/')
def index():
    return "Hello World!"
    
@app.route('/upload/<name>')
def upload(name):
    print(name)
    return "Upload"