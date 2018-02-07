import os

from logger import *

BASE_DIR = os.path.dirname(__file__)
UPLOADS_DIR = os.path.join(BASE_DIR, 'static', 'uploads')

# HTML Pages

def handle_index(entry,values):
  images = []

  def getmtime(name):
    path = os.path.join(UPLOADS_DIR, name)
    return os.path.getmtime(path)

  for file in sorted(os.listdir(UPLOADS_DIR), key=getmtime, reverse=True):
    image = os.path.join('uploads', file)
    images.append(image)

  dict = {}
  dict['images'] = images

  return dict
