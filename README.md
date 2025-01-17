# Introduction

This homegrown Naive Bayesian Classifier is a cli-application that can classify Tweets based upon some training data.

# How To Use

Python 3.7 or higher is required.

## Requirements

The dependencies in ```requirements.txt``` are needed to both run the cli-application and develop and test the program. To install all the dependencies, run the following command (ensure that your current working directory is in the top level of the cloned repo):

```bash
pip install -r requirements.txt

# you can also verify if installation succeeded by running the following
$ pip list
```

You will first need to install the program on your machine. A virtual environment is recommended.

```bash
$ python3 -m venv nbc_env
$ source nbc_env/bin/activate
$ pip install --editable .
```

To view the available commands, execute the following command:

```bash
$ nbc

>>>
usage: nbc [-h] [-v] {train,classify} ...

Naive Bayesian Classifier that classifies tweets

positional arguments:
  {train,classify}
    train           train help
    classify        classify help

optional arguments:
  -h, --help        show this help message and exit
  -v, --version     show version and exit

```

The following command classifies a test Tweet from this repo's sample training data

```bash
# classify takes two arguments:
# the first argument is a path to the training data
# the second argument is a Tweet
$ nbc classify data/training_data.csv 'America must decide between failed policies or fresh perspective, a corrupt system or an outsider'
```

# Development

First, install all the requirements. See the Requirements subsection above.

Python 3.7+ is required. A virtual environment is highly recommended. Simply clone and install in "editable mode" (--editable, -e):

```bash
$ python3 -m venv nbc_env
$ source nbc_env/bin/activate
$ pip install --editable .
```

## Testing

To run the tests with verbose and to see any print statements, run the following command:

```bash
$ pytest --capture=no -v
```

To view code coverage, run the following commands:

```bash
$ coverage run --source=src --omit="src/nbc_cli.py","src/eval*" -m pytest
# To view coverage report on the command line:
$ coverage report -m

# To view coverage report on a local browser
$ coverage html
$ open htmlcov/index.html
```
