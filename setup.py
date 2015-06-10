#!/usr/bin/env python
from setuptools import setup
from wez import __version__ as version


def fread(filepath):
    with open(filepath, 'r') as f:
        return f.read()


setup(
    name='wez',
    version=version,
    include_package_data=True,
    install_requires=[
        'requests',
    ],
    zip_safe=False,
    py_modules=['wez'],
    entry_points={
        'console_scripts': [
            'wez = wez:main',
        ]
    },
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
    license="MIT",
    description='',
    long_description=fread('README.rst'),
    author='Kane Blueriver',
    author_email='kxxoling@gmail.com',
    url='https://github.com/kxxoling/wez',
)
