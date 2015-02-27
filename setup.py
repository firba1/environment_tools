#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

setup(
    name='environment_tools',
    version='0.0.1',
    description='Utilities for describing Yelp hardware environments',
    packages=['environment_tools'],
    setup_requires=['setuptools'],
    install_requires=[
        'simplejson >= 2.1.0',
    ],
    entry_points={
        'console_scripts': []
    },
    license='Copyright Yelp 2015, All Rights Reserved',
    include_package_data=True
)