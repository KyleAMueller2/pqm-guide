#!/bin/bash

cd docs
pipenv run sphinx-build -b html . ../_build
