#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 25 17:23:32 2020

@author: jeanwolf
"""
# pyqrcode; Image y PIL son las dependencias requeridas
# pyqrcode genera los QR
# Image convierte un png a JPG

import pyqrcode
from PIL import Image
import os, sys

try:
    os.mkdir('imagen')
except OSError as e:
    if e.errno != errno.EEXIST:
        raise


# crear QR
url =  pyqrcode.create('0987654321', error='L', version=4, mode='binary')
url.svg('imagen/code.svg', scale=16)

# crear PNG
big_code = pyqrcode.create('0987654321', error='L', version=4, mode='binary')
big_code.png('imagen/code.png', scale=10, module_color=[0, 0, 0, 128], background=[0xFF, 0xFF, 0xFF])

# convertir PNG a JPG
im = Image.open('code.png')
rgb_im = im.convert('RGB')
rgb_im.save('imagen/code.jpg', quality=95)

