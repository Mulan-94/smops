#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages


setup(
    entry_points={
        'console_scripts': [
            'smops=smops.smooth:main',
        ],
    },
    packages=find_packages(include=['smops', 'smops.*']),
)
