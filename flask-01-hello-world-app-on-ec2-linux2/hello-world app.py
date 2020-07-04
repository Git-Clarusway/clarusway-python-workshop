#hello-world app.py
from flask import Flask

app=Flask(__name__)

@app.route('/')
def hello():
    return 'hello world'

if __name__=='__main__':
    app.run(debug=True) 
    # app.run('localhost',port=80)
    app.run('0.0.0.0',port=80)