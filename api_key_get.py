import os
import json
import urllib
import urllib.request
from urllib.request import urlopen
from urllib.parse import quote
import re
def get_api():
        api_url='https://openapi.baidu.com/oauth/2.0/token?grant_type=client_credentials&client_id=7vz7Sdza6MUoRSYwzMAVGsAS&client_secret=WwYiaE7jBnN6GFPDh7hOfvQN5uGmIwyz'
        result=str(urlopen(api_url).read(),encoding=('utf-8'))
        api_dict=json.loads(result)
        api_token=api_dict['access_token']
        return api_token
print(get_api())
