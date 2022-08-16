#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
    name='requestbin',
    version='2.0.0',
    author='Runscope',
    description='HTTP request collector and inspector',
    packages=find_packages(),
    install_requires=['feedparser'],
    data_files=[],
)
