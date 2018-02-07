#!/usr/bin/python

import os, sys, email, re, tempfile, cStringIO, base64
from PIL import Image

from logger import *

IMAGE_MAX_SIZE = 1024

BASE_DIR = os.path.dirname(__file__)

data = sys.stdin.read()

mail = email.message_from_string(data)

if mail.is_multipart():
  for part in mail.get_payload():
    if part.get_content_type().startswith('image'):
      payload = part.get_payload(decode=True)
      try:
        im = Image.open(cStringIO.StringIO(payload))
        # Ensure it is no bigger than this
        im.thumbnail((IMAGE_MAX_SIZE,IMAGE_MAX_SIZE), Image.ANTIALIAS)
        data = cStringIO.StringIO()
        im.save(data, 'JPEG')
        #message = 'data:image/jpg;base64,' + base64.b64encode(data.getvalue())

        (fd,filename) = tempfile.mkstemp(dir=os.path.join(BASE_DIR, 'static', 'uploads'), prefix='uploads-', suffix='.jpg')
        with os.fdopen(fd, 'w') as f:
          f.write(data.getvalue())
          f.close()
          os.chmod(filename,0444)
      except Exception as e:
        logger.error('ERROR: upload: %s' % e)
