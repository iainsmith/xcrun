#!/usr/bin/env python

from setuptools import setup, find_packages
from os import path


setup(name='xcrun',
      version='0.1',
      description='Python wrapper around the xcrun utility',
      url='https://github.com/dalemyers/xcrun',
      author='Dale Myers',
      author_email='dale@myers.io',
      license='MIT',
      packages=['xcrun'],
      zip_safe=False)


here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md')) as f:
    long_description = f.read()

setup(
    name='xcrun',
    version='0.1',
    description='Python wrapper around the xcrun utility',
    long_description=long_description,
    url='https://github.com/dalemyers/xcrun',
    author='Dale Myers',
    author_email='dale@myers.io',
    license='MIT',

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: MacOS X',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: MacOS :: MacOS X',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Build Tools',
        'Topic :: Software Development :: Testing',
        'Topic :: Utilities'
    ],

    keywords='xcode xcrun simctl ios simulator',
    packages=find_packages(exclude=['docs', 'tests'])
)