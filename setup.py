from setuptools import setup


if __name__ == '__main__':
  setup(
    name='Flask-NSQ',
    description="Simple interface for using NSQ with Flask",
    version='0.0.1',
    py_modules=['flask_nsq'],
    author="Mark Steve Samson <hello@marksteve.com>",
    install_requires=[
      'pynsq>=0.4,<0.5',
      'requests>=1.0,<1.3',
      'msgpack-python>=0.3,<0.4',
    ],
    zip_safe=False,
  )
