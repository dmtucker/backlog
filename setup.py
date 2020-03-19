"""A setuptools based setup module.

See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""


import codecs
import os.path

import setuptools  # type: ignore


def read(*parts):
    """Read a file in this repository."""
    here = os.path.abspath(os.path.dirname(__file__))
    with codecs.open(os.path.join(here, *parts), 'r') as file_:
        return file_.read()


ENTRY_POINTS = {'console_scripts': ['backlog = backlog.cli:main']}


if __name__ == '__main__':
    setuptools.setup(
        name='backlog',
        use_scm_version=True,
        description='A Glorified TODO list',
        long_description=read('README.rst'),
        long_description_content_type='text/x-rst',
        author='David Tucker',
        author_email='david@tucker.name',
        license='LGPLv2+',
        url='https://pypi.org/project/backlog',
        project_urls={
            'Code': 'https://github.com/dmtucker/backlog',
            'Documentation': 'https://dmtucker.github.io/backlog',
            'Issues': 'https://github.com/dmtucker/backlog/issues',
        },
        package_dir={'': 'src'},
        packages=setuptools.find_packages('src'),
        include_package_data=True,
        setup_requires=['setuptools_scm >= 3.5'],
        python_requires='>= 3.7',
        install_requires=[
            'click >= 7.1',
            'setuptools >= 46.1',
        ],
        entry_points=ENTRY_POINTS,
        keywords='notes backlog todo list',
        classifiers=[
            'License :: OSI Approved :: '
            'GNU Lesser General Public License v2 or later (LGPLv2+)',
            'Intended Audience :: End Users/Desktop',
            'Programming Language :: Python :: 3.7',
            'Programming Language :: Python :: 3.8',
            'Development Status :: 5 - Production/Stable',
        ],
    )
