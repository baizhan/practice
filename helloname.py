from flask import Flask
app=Flask(__name__)
@app.route('/')
def home():
    return '主页'
@app.route('/user/<name>/')
def user(name):
    return '您好，%s'%name
if __name__=='__main__':
    app.run()
