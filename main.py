from http.server import HTTPServer, SimpleHTTPRequestHandler

from jinja2 import Environment, FileSystemLoader, select_autoescape

import datetime

env = Environment(
    loader=FileSystemLoader('.'),
    autoescape=select_autoescape(['html', 'xml'])
)

template = env.get_template('template.html')


def get_delta_year():
    date_foundation = datetime.datetime(year=1920,month=1, day=1)
    date_now = datetime.datetime.now()
    delta = date_now - date_foundation
    seconds = delta.total_seconds()
    years = seconds / 60 / 60 / 24 / 365
    return int(years)


rendered_page = template.render(
    delta_year = get_delta_year()
)

with open('index.html', 'w', encoding="utf8") as file:
    file.write(rendered_page)

server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
server.serve_forever()