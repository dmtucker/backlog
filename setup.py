#!/usr/bin/env python3

"""A setuptools based setup module.

See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""


import codecs
import os.path
import re

import setuptools  # type: ignore


def read(*parts):
    """Read a file in this repository."""
    here = os.path.abspath(os.path.dirname(__file__))
    with codecs.open(os.path.join(here, *parts), 'r') as file_:
        return file_.read()


def find_version(*file_paths):
    """
    Read the file in setup.py and parse the version with a regex.

    https://packaging.python.org/guides/single-sourcing-package-version/
    """
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


setuptools.setup(
    name='backlog',
    version=find_version('src', 'backlog', '__init__.py'),
    description='A Glorified TODO list',
    long_description=read('README.rst'),
    author='David Tucker',
    author_email='david@tucker.name',
    license='LGPLv2+',
    url='https://github.com/dmtucker/backlog',
    package_dir={'': 'src'},
    packages=setuptools.find_packages('src'),
    include_package_data=True,
    python_requires='~=3.6',
    install_requires=[
        'attrs~=17.4',
        'click~=6.7',
    ],
    entry_points={'console_scripts': ['backlog = backlog.cli:main']},
    keywords='notes backlog todo list',
    classifiers=[
        'License :: OSI Approved :: '
        'GNU Lesser General Public License v2 or later (LGPLv2+)',
        'Intended Audience :: End Users/Desktop',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Development Status :: 5 - Production/Stable',
    ],
)
