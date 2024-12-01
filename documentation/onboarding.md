# Installation and update

## Installation

* Create virtual environment
In the root of the repository

```bash
python3 -m venv .venv
```

* Activate the environemnt

```bash
source .venv/bin/activate
```

* Install packages

```bash
pip install -r requirements/base.txt
```

## Update

* Update pip. Execute whithin the environment

```bash
python -m pip install --upgrade pip
```

* Update all the packages

```bash
pip install -r requirements/base.txt --upgrade
```