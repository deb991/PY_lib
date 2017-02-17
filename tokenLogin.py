#!/usr/bin/ env python
import os
import sys
import random
import math
import requests
import cookielib
import urllib
import urllib2
import webbrowser


__author__ = 'JsOzz'

url = 'https://www.facebook.com'
webbrowser.open_new(url)
values = {'Email or Phone-clear': 'Combination',
          'Email or Phone-email': '9748412981',
          'password-clear': 'Combination',
          'password-password': 'minimumx2'}

data = urllib.urlencode(values)
cookies = cookielib.CookieJar()

opener = urllib2.build_opener(
    urllib2.HTTPRedirectHandler(),
    urllib2.HTTPHandler(debuglevel=0),
    urllib2.HTTPSHandler(debuglevel=0),
    urllib2.HTTPCookieProcessor(cookies))

response = opener.open(url, data)
the_page = response.read()
http_headers = response.info()
# The login cookies should be contained in the cookies variable
