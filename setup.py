import os
import ez_setup

ez_setup.use_setuptools()

from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

with open("requirements.txt") as requirements:
    install_requires = requirements.readlines()

setup(
    name="waas",
    version="0.1",
    author="Brendan Donegan",
    author_email="brendan.j.donegan@gmail.com",
    description=("A simple application that prints out the weather "
                 "at your current location, or for a specified IP."),
    setup_requires=['coverage', 'nose>=1.0'],
    install_requires=install_requires,
    test_suite='waas.tests',
    keywords="weather",
    long_description=read("README.md"),
    entry_points={
        'console_scripts': [
            'waas = waas.waas:main'
        ]
    }
)
