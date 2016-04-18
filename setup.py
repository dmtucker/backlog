#!/usr/bin/env python

"""A setuptools based setup module.

See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

from setuptools import setup, find_packages
import backlog

with open('README.md') as readme_file:
    README = readme_file.read()

setup(
    name='backlog',
    version=backlog.__version__,
    description=backlog.__doc__,
    long_description=README,
    license='LGPLv2+',
    url='https://github.com/dmtucker/backlog',
    author='David Tucker',
    author_email='david.michael.tucker@gmail.com',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: '
        'GNU Lesser General Public License v2 or later (LGPLv2+)',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ],
    keywords='notes backlog todo lists',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    entry_points={'console_scripts': ['backlog=backlog.__main__:main']},
)
