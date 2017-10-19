#!/bin/bash
VENV=venv

virtualenv -p python3 $VENV
source $VENV/bin/activate
pip3 install -r requirements.txt
