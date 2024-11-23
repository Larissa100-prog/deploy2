#!/usr/bin/env bash

python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt

python3 manage.py makemigrations --noinput
python3 manage.py migrate --noinput