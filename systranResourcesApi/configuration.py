"""
Copyright 2015 SYSTRAN Software, Inc. All rights reserved.

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from __future__ import absolute_import
import base64
import urllib3
import sys

def load_api_key(api_key_file):
    try:
        f = open(api_key_file, "r")
        key = f.read().strip()
        if key == '':
            # The key file should't be blank
            print('The api_key.txt file appears to be blank, please paste YOUR_API_KEY here')
            sys.exit(0)
        else:
            # setup the key
            global api_key
            api_key["key"] = key

        f.close()
    except IOError:
        # The file doesn't exist, so show the message and create the file.
        print('API Key not found!')

        # create a blank key file
        open('api_key.txt', 'a').close()
        sys.exit(0)
    except Exception as e:
        print(e)

def get_api_key_with_prefix(key):
    global api_key
    global api_key_prefix

    if api_key.get(key) and api_key_prefix.get(key):
      return api_key_prefix[key] + ' ' + api_key[key]
    elif api_key.get(key):
      return api_key[key]

def get_basic_auth_token():
    global username
    global password

    return urllib3.util.make_headers(basic_auth=username + ':' + password).get('authorization')

def auth_settings():
    return { 
               'apiKey': {
                   'type': 'api_key',
                   'in': 'query',
                   'key': 'key',
                   'value': get_api_key_with_prefix('key')
               },
             
               'accessToken': {
                   'type': 'api_key',
                   'in': 'header',
                   'key': 'Authorization',
                   'value': get_api_key_with_prefix('Authorization')
               },
             
           }

# Default Base url
host = "https://api-platform.systran.net"

# Default api client
api_client = None
             
# Authentication settings
api_key = {}
api_key_prefix = {}
username = ''
password = ''


