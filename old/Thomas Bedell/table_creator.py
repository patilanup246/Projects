from flask import Flask
from flask import request
app = Flask(__name__)

@app.route('/export')
def index():
    return open('Zillow_Listing_2017-08-04.csv','r').read()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8080')
