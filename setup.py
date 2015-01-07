#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='drf-fsm-transitions',
    version='0.2.0',
    description='Automatically hook your Django-FSM transitions up to Django REST Framework',
    author='Jacob Haslehurst',
    author_email='jacob@haslehurst.net',
    url='https://github.com/hzy/drf-fsm-transitions',
    packages=find_packages(),
    install_requires=['django', 'django_fsm', 'djangorestframework']
)
