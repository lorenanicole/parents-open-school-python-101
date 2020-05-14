#!/usr/bin/env python
#  -*- coding: utf-8 -*-

"""
Script to use the CatAPI: https://thecatapi.com/

You can run from the commandline with: python basic_cat.py
"""

__author__      = "Lorena Mesa"
__email__       = "me@lorenamesa.com"
__status__      = "Teaching"

import requests
from PIL import Image

response = requests.get('https://api.thecatapi.com/v1/images/search')

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