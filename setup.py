import os
from setuptools import setup, find_packages

# Utility function to read the README file.
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

# We do this because we want to be able to install JUST the
# dependencies when modifying code.
def read_requirements():
    file = read('requirements.txt')
    return file.split('\n')

setup(
    name             = "sour",
    version          = "1.0.0",
    author           = "et al",
    author_email     = "asd",
    description      = ("Sauerbraten utils"),
    long_description = read('README.md'),
    packages         = find_packages(exclude=['test']),
    classifiers      = [],
    scripts          = [],
    install_requires = read_requirements()
)
