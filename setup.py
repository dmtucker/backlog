#!/usr/bin/env python
# coding: utf-8

"""A setuptools based setup module.

See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

from __future__ import absolute_import
from setuptools import setup, find_packages
import backlog

with open('README.rst') as readme_file:
    README = readme_file.read()

setup(
    name='backlog',
    version=backlog.__version__,
    description=backlog.__doc__,
    long_description=README,
    author='David Tucker',
    author_email='david.michael.tucker@gmail.com',
    license='LGPLv2+',
    url='https://github.com/dmtucker/backlog',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    include_package_data=True,
    entry_points={'console_scripts': ['backlog=backlog.__main__:main']},
    keywords='notes backlog todo lists',
    classifiers=[
        'License :: OSI Approved :: '
        'GNU Lesser General Public License v2 or later (LGPLv2+)',
        'Intended Audience :: End Users/Desktop',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Development Status :: 4 - Beta',
        ],
)
