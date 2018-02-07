import datetime, random

from detectmobilebrowser import *

TITLE    = 'Kai Eves Photography'
SUBTITLE = 'Professional Photography Services'
YEAR     = datetime.date.today().year

DOMAIN   = 'KaiEvesPhotography.com'
URL      = 'www.' + DOMAIN.lower()
WWW      = 'http://' + URL
CGI      = 'http://' + URL + '/cgi-bin' # TODO change to https://

PROMO    = 'Quality Software Services'

#PUBLISHERS = ['bannerplay','amazon-us-1','amazon-us-2','amazon-us-3','revenuehits']
PUBLISHERS = ['google']

def html_defaults(user_agent=None):
  return {
    'domain':     DOMAIN,
    'www':        WWW,
    'cgi':        CGI,
    'title':      TITLE,
    'subtitle':   SUBTITLE,
    'year':       YEAR,
    'promo':      PROMO,
    'publisher1': PUBLISHERS[random.randint(0,len(PUBLISHERS)-1)],
    'publisher2': PUBLISHERS[random.randint(0,len(PUBLISHERS)-1)],
    'is_mobile':  is_mobile_browser(user_agent)
  }
