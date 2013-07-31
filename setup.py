# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

import WSTSFU as project

with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name=project.__name__,
    version=project.__version__,
    description=project.__description__,
    long_description=readme,
    author=project.__author__,
    author_email=project.__author_email__,
    url=project.__url__,
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

