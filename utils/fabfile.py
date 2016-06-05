# -*- coding: utf-8 -*-

"""
Command: fab update
"""

from __future__ import absolute_import, unicode_literals

from fabric.api import *

import properties as props

# Credentials:
env.hosts = [getattr(props, 'SERVER_IP'), ]  # IP and SSH port
env.user = getattr(props, 'SERVER_USER')  # Unix user
env.app = getattr(props, 'SERVER_APP')  # Supervisor service
env.APP_DIR = getattr(props, 'SERVER_APP_DIR')  # Project directory
env.virtualenv = getattr(props, 'SERVER_VIRTUALENV')  # Virtualenv
env.key_filename = [getattr(props, 'SERVER_PATH_PEM')]  # Security key

ACTIVATE_VIRTUALENV = 'source /home/ubuntu/.virtualenvs/{}/bin/activate' \
    .format(env.app)


def update():
    git()
    requirements()
    migrate()
    collectstatic()
    clean_pyc()
    restart()


def git():
    """ git pull """
    with cd(env.APP_DIR):
        run('git pull origin master')


def gitstatus():
    """ git status """
    with cd(env.APP_DIR):
        run('git status')


def requirements():
    """ pip install -r requirements.txt """
    with cd(env.APP_DIR):
        with prefix(ACTIVATE_VIRTUALENV):
            run('pip install -r requirements.txt')


def migrate():
    """ python manage.py migrate """
    with cd(env.APP_DIR):
        with prefix(ACTIVATE_VIRTUALENV):
            run('python manage.py migrate')


def collectstatic():
    """ python manage.py collectstatic """
    with cd(env.APP_DIR):
        with prefix(ACTIVATE_VIRTUALENV):
            run('python manage.py collectstatic --noinput')


def clean_pyc():
    """ python manage.py clean_pyc """
    with cd(env.APP_DIR):
        with prefix(ACTIVATE_VIRTUALENV):
            run('python manage.py clean_pyc')


def status():
    """ sudo supervisorctl status pdepou """
    run('sudo supervisorctl status %s' % env.app)


def stop():
    """ sudo supervisorctl stop pdepou """
    run('sudo supervisorctl stop %s' % env.app)


def start():
    """ sudo supervisorctl start pdepou """
    run('sudo supervisorctl start %s' % env.app)


def restart():
    """ sudo supervisorctl restart pdepou """
    run('sudo supervisorctl restart %s' % env.app)
    status()
