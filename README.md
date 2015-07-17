# markov

Command line tool to generate Markov chain given set of files.

## Prerequisites

You'll need the following installed:

* [Python 2.x](https://www.python.org/)
* [Virtualenv](https://virtualenv.pypa.io/)

If this command gives you a version number, you are good to go:

    $ virtualenv --version

## Getting started

### Creating and activating virtualenv

    $ virtualenv venv --no-site-packages # Only once
    $ source venv/bin/activate # Every time

### Installing dependencies in virtualenv

    $ pip install -r requirements.txt

### Running the app

    $ ./markov.py -v ~/my-documents/*
    $ ./markov.py -h # for help
    