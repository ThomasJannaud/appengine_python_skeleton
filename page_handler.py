import jinja2
import os

import flask
from flask import request

jinja_environment = jinja2.Environment(
    autoescape=False,
    loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), 'Templates')))


def StaticPageHandler(request_path):
    request_path = request_path[:-1] if request_path.endswith('/') else request_path
    template_name = "contact" if request_path == "/contact" else "home"
    template_vars = {"name": request.args.get("name")}
    j_tmpl = jinja_environment.get_template('%s.html' % template_name)
    resp = flask.make_response(j_tmpl.render(template_vars))
    return resp
