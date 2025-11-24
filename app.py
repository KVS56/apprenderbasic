from flask import Flask
app = Flask(__name__)

@app.route('/')
def flying_dutchman():
    return 'flying dutchman'
