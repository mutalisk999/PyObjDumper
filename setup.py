#!/usr/bin/env python
# encoding: utf-8

from setuptools import setup

VERSION = '0.0.1'
DESCRIPTION = ""
LONG_DESCRIPTION = """
"""

setup(
    name="PyObjDumper",
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    keywords=('PyObjDumper', 'pydantic'),
    author="mutalisk999",
    author_email="",
    url="https://github.com/mutalisk999/PyObjDumper",
    license="MIT License",
    platforms=['any'],
    test_suite="",
    zip_safe=True,
    install_requires=['pydantic>=1.8.2'],
    packages=['PyObjDumper']
)