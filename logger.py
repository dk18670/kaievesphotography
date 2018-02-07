import logging

logger = logging.getLogger('kaievesphotography')
logging.basicConfig(format='%(asctime)-15s %(message)s', filename='/var/log/kaievesphotography/log', level=logging.DEBUG)
