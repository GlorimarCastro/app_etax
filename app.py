'''
Created on Jan 16, 2018

@author: galarwen
'''

from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route('/')
def test():
    return 'Hello World'

@app.route('/login')
def login():
    return render_template('example.html')

if __name__ == '__main__':
    app.run()