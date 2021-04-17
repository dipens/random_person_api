import urllib.request
import json


def make_request_call(url):
    return json.loads(urllib.request.urlopen(url).read())