from app import app


@app.route('/')
@app.route('/index')
def index():
    return "Hello, Welcome to the Sensu Contacts app."
