import os
from PIL import Image

from logger import *

BASE_DIR = os.path.dirname(__file__)
STATIC_DIR = os.path.join(BASE_DIR, 'static')
UPLOADS_DIR = os.path.join(STATIC_DIR, 'uploads')

# HTML Pages

def handle_index(entry,values):
  images = []

  def getmtime(name):
    path = os.path.join(UPLOADS_DIR, name)
    return os.path.getmtime(path)

  for file in sorted(os.listdir(UPLOADS_DIR), key=getmtime, reverse=True):
    url = os.path.join('uploads', file)
    im = Image.open(os.path.join(STATIC_DIR, url))
    width, height = im.size
    image = {
      'url': url,
      'width': width,
      'height': height,
      'header': file,
      'caption': file,
    }
    images.append(image)

  dict = {}
  dict['images'] = images

  return dict
