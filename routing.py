from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return 'Home Page'

@app.route('/admin')
def admin():
    return 'Admin page'


    