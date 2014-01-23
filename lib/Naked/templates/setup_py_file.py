#!/usr/bin/env python
# encoding: utf-8

# VARS: app_name, developer, license
setup_py_string = """
import os
from setuptools import setup, find_packages
from Naked.commands.version import Version


def file_read(fname):
    return open(os.path.join(os.path.dirname(__file__), 'docs', fname)).read()

setup(
    name='{{app_name}}',
    version=Version().get_version(),
    description='',
    long_description=(file_read('README.rst')),
    url='',
    license='{{license}}',
    author='{{developer}}',
    author_email='',
    platforms=['any'],
    entry_points = {
        'console_scripts': [
            '{{app_name}} = {{app_name}}.app:main'
        ],
    },
    packages=find_packages("lib"),
    package_dir={'': 'lib'},
    install_requires=['Naked'],
    keywords='',
    include_package_data=True,
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3'
    ],
)
"""
