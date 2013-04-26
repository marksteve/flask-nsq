import requests
import msgpack
import nsq


class NSQ(object):

  config = dict()

  def __init__(self, app=None):
    if app:
      self.app = app
      self.init_app(app)

  def init_app(self, app):
    self.config.update(
      nsqd_host=app.config.get('NSQD_HOST', 'http://127.0.0.1:4151'),
    )

  def serialize(self, message):
    return msgpack.packb(message)

  def publish(self, topic, message):
    r = requests.post(self.config['nsqd_host'] + '/put',
                      params=dict(topic=topic),
                      data=self.serialize(message))
    r.raise_for_status()
    return r.content


class Consumer(object):
  tasks = {}

  def __init__(self, tasks=None, **config):
    if tasks:
      map(self.add_task, tasks.items())
    self.config = config

  def add_task(self, name, func):
    self.tasks[name] = func
    return self

  def remove_task(self, name):
    self.pop(name)
    return self

  def run(self):
    self.reader = nsq.Reader(
      self.tasks,
      topic=self.config['topic'],
      channel=self.config['channel'],
      nsqd_tcp_addresses=self.config.get('nsqd_tcp_addresses',
                                         ['127.0.0.1:4150']),
      max_in_flight=self.config.get('max_in_flight', 1))
    nsq.run()
