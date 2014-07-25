#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Redmine Statusboard

from __future__ import unicode_literals

from flask import Flask, render_template
import arrow

from utils import get_issues

# Build Flask instance with its config
app = Flask(__name__)
app.config.from_pyfile('config.py')


@app.route('/')
def index():
    return render_template('index.html', issues=get_issues())


@app.route('/favicon.ico')
def favicon():
    return app.send_static_file('img/favicon.ico')


# Custom filter used in the template
@app.template_filter('humanize_date')
def _humanize_date_from_string(string):
    """
    Humanize a date
    """
    return arrow.get(string).humanize(locale='fr')

if __name__ == '__main__':
    app.run()
