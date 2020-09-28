#!/usr/bin/env python
from setuptools import setup

PACKAGE_NAME = 'python-foreman'
URL = 'https://github.com/kcl-nmssys/python-foreman'


if __name__ == '__main__':
    setup(
        install_requires=[
            'requests',
            'six',
        ],
        name=PACKAGE_NAME,
        version='0.3.4',
        include_package_data=True,
        packages=['foreman'],
        description=(
            'Simple low-level client library to access the Foreman API'
        ),
        author='David Caro',
        author_email='david@dcaro.es',
        url=URL,
        bugtracker_url=URL + '/issues/',
        license='GPLv2',
        classifiers=[
            'Intended Audience :: Developers',
            'Intended Audience :: Information Technology',
            'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
            'Operating System :: OS Independent',
            'Programming Language :: Python',
            'Programming Language :: Python :: 2.7',
            'Programming Language :: Python :: 3.4',
        ],
    )
