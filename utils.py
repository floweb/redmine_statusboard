#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Redmine Statusboard
# utils.py

from __future__ import unicode_literals

from flask import current_app as app
from redmine import Redmine


def get_issues(filter='open'):
    """
    Thanks to Python-Redmine, we get the issues for our statusboard
    """
    redmine = Redmine(url=app.config['REDMINE_URL'],
                      key=app.config['REDMINE_KEY'])

    return redmine.issue.filter(status_id=filter,
                                project_id=app.config['REDMINE_PROJECT'])
