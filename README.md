# A RealEstate
The Django project on Real estate portal for 2nd year IT branch

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

You're going to need the tools below to run on your machine

* [python](https://www.python.org) -python
* [virtualenv](http://docs.python-guide.org/en/latest/dev/virtualenvs/) -virtualenv

### Installing

A step by step series of examples that tell you have to get a development env running

First install python and virtualenv.

* [python](https://www.python.org/downloads/) - python programming language

> pip install virtualenv

create and activate the virtual environment

```
virtualenv venv && source bin/activate
pip install -r requirements.txt
python manage.py migrate
```
