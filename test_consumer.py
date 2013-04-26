import logging

from flask.ext.nsq import Consumer
import msgpack


logging.root.setLevel(logging.DEBUG)


def print_message(message):
  print msgpack.unpackb(message.body)
  message.finish()


c = Consumer(topic='mailer', channel='send')
c.add_task('print_message', print_message)
c.run()
