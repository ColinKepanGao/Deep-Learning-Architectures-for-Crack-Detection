# -*- coding: utf-8 -*-
"""TACK_vectorization.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1GMd45DPI8pFaWbcQYpM6vr9xkCR4W5uc
"""

!pip install centerline

!pip install grass

!gdal_polygonize.py

from google.colab import drive
drive.mount('/content/drive/')

!gdal_polygonize.py "/content/drive/My Drive/Colab Notebooks/TACK/Large/fuse/Camera4_block2-gata1_2017-10-10_231224_000101_D.bmp___fuse.png" -mask "/content/drive/My Drive/Colab Notebooks/TACK/Large/fuse/Camera4_block2-gata1_2017-10-10_231224_000101_D.bmp___fuse.png" "/content/drive/My Drive/Colab Notebooks/TACK/Large/fuse/Camera4_block2-gata1_2017-10-10_231224_000101_D.bmp___fuse.geojson"

!create_centerlines "/content/drive/My Drive/Colab Notebooks/TACK/Large/fuse/Camera4_block2-gata1_2017-10-10_231224_000101_D.bmp___fuse.geojson" "/content/drive/My Drive/Colab Notebooks/TACK/Large/fuse/Camera4_block2-gata1_2017-10-10_231224_000101_D.bmp___fuse_centerline.geojson"

import os
path_mask = '/content/drive/My Drive/Colab Notebooks/TACK/Large/fuse/Camera4_block2-gata1_2017-10-10_231224_000101_D.bmp___fuse.png'
path_polygon = '/content/drive/My Drive/Colab Notebooks/TACK/Large/fuse/Camera4_block2-gata1_2017-10-10_231224_000101_D.bmp___fuse.geojson'
os.system('!gdal_polygonize.py ' + path_mask + ' -mask ' + path_mask + ' ' + path_polygon)