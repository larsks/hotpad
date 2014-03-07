#!/usr/bin/env python

from setuptools import setup

setup(name='hotpad',
      version='1.0',
      description='High-level wrappers for OpenStack Heat',
      author='Lars Kellogg-Stedman',
      author_email='lars@oddbit.com',
      url='http://github.com/larsks/hotpad',
      install_requires=open('requirements.txt').readlines(),
      )

