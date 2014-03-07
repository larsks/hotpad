#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='hotpad',
    version='1.0',
    description='High-level wrappers for OpenStack Heat',
    author='Lars Kellogg-Stedman',
    author_email='lars@oddbit.com',
    url='http://github.com/larsks/hotpad',
    install_requires=open('requirements.txt').readlines(),
    packages=find_packages(),
    entry_points = {
        'console_scripts': [
            'heat-output = hotpad.commands.heat_output:main',
            'dotstack = hotpad.commands.dotstack:main',
        ],
    }
)

