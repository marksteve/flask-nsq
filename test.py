from flask import Flask
from flask.ext.nsq import NSQ


app = Flask(__name__)
nsq = NSQ(app)


@app.route('/send_mail')
def send_mail():
  return nsq.publish('mailer', dict(
    id='welcome',
    sender='sender@gmail.com',
    recipient='recipient@gmail.com',
    subject='Hello, world',
    body='All your base are belong to us.',
  ))


app.run(debug=True)
