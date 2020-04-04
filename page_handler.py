import jinja2
import logging
import os

import flask
from flask import redirect
from flask import request

jinja_environment = jinja2.Environment(
  autoescape=False,
  loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), 'Templates')))


# urls:
# /contact for the contact page,
# / for the home page. The home page accepts an optional 'name' GET parameter, and greets with that name
# any other url redirects to the home page
def StaticPageHandler(request_path):
  logging.info("new request on %s", request_path)
  request_path = request_path[:-1] if request_path.endswith('/') and request_path != '/' else request_path
  if request_path not in ('/', '/contact'):
    return redirect('/')  # redirect to home page
  template_name = "contact" if request_path == "/contact" else "home"
  template_vars = {"name": request.args.get("name")}
  j_tmpl = jinja_environment.get_template('%s.html' % template_name)
  resp = flask.make_response(j_tmpl.render(template_vars))
  return resp
