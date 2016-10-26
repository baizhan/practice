from flask import Flask,render_template
from flask.ext.mail import Mail,Message
import os
app=Flask(__name__)
app.config['MAIL_SERVER']='SMTP.163.COM'#电子邮件的服务器或主机名
app.config['MAIL_PORT']='25'#电子邮件服务器的端口
app.config['MAIL_USE_TLS']=True
app.config['MAIL_USERNAME']=os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD']=os.environ.get('MAIL_PASSWORD')
mail=Mail(app)
@app.route('/')
def index2():
    msg=Message('主题',sender=os.environ.get('MAIL_USERNAME'),recipients=['test@test.com'])
    msg.body='文本 body'
    msg.html='<b>HTML</b>Body'
    mail.send(msg)
    return '<h1>邮件发送成功</h1>'
if __name__=='__main__':
    app.run(debug=True)