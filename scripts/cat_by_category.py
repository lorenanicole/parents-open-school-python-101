#!/usr/bin/env python
#  -*- coding: utf-8 -*-

"""
Script to use the CatAPI: https://thecatapi.com/

To use you'll need to register to use the CatAPI and obtain
an API key via email, insert the following value into the
`.env` file:
- GITHUB_TOKEN

You can run from the commandline with: python cat_by_category.py
"""

__author__      = "Lorena Mesa"
__email__       = "me@lorenamesa.com"
__status__      = "Teaching"

from os import getenv
import requests
from PIL import Image

CAT_API = 'https://api.thecatapi.com/v1'
CAT_API_KEY = getenv('CAT_API_KEY')

categories = requests.get(f"{CAT_API}/categories", headers={"x-api-key": CAT_API_KEY})

if categories.ok:
    print(f"Here are categories:\n")
    for category in categories.json():
        print(f"ID: {category.get('id')} - {category.get('name')}")
    category_id = input("Which category do you want to use? Please enter the id of the category number only e.g. 1: ")
    print(f"Great! You've selected {category_id}!")

response = requests.get(f"{CAT_API}/images/search?category_ids={category_id}", headers={"x-api-key": CAT_API_KEY})

if not response.ok:
    print("Error! Try again!")

images = response.json()

for image in images:
    image_url = image.get('url')
    image_response = requests.get(image_url, stream=True)
    if image_response.ok:
        image = Image.open(image_response.raw)
        image.show()
    else:
        print("Unable to get cat image! Try again!")