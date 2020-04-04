import logging
from flask import Flask
from flask_talisman import Talisman

app = Flask(__name__)
Talisman(app, content_security_policy=None)  # automatic redirection of http to https

import page_handler

logging.getLogger().setLevel(logging.INFO)

@app.route('/')
def handleHome():
  return page_handler.StaticPageHandler('/')

@app.route('/<path:path>')
def handle(path):
  return page_handler.StaticPageHandler('/' + path)


if __name__ == '__main__':
    # This is used when running locally. Gunicorn is used to run the
    # application on Google App Engine. See entrypoint in app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
