from flask import Flask
from datetime import datetime
app = Flask(__name__)

@app.route('/')
def flying_dutchman():
    return render_template('index.html')
    

@app.route('/sister')
def sheistywearer():
    return 'aishwaya is my sister and she loves to commit CRIMES that are ILLEGAL because she is EVIL and a BAD person. also she is cute.'
