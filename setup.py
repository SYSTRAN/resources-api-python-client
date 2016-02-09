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

import sys
from setuptools import setup, find_packages



# To install the library, open a Terminal shell, then run this
# file by typing:
#
# python setup.py install
#
# You need to have the setuptools module installed.
# Try reading the setuptools documentation:
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.10", "six >= 1.9", "certifi"]

setup(
    name="resources-api-python-client",
    version="1.0.2",
    description="Rest Resource API",
    author_email="",
    url="",
    keywords=["Systran", "Rest Resource API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    ### Introduction\n\nREST API to manage SYSTRAN resources used in translation: corpora and dictionaries.\n\n### Cross Domain\n\nResource API supports cross-domain requests through the JSONP or the CORS mechanism.\n\nResource API also supports the Silverlight client access policy file (clientaccesspolicy.xml) and the Adobe Flash cross-domain policy file (crossdomain.xml) that handles cross-domain requests.\n\n#### JSONP Support\n\nResource API supports JSONP by providing the name of the callback function as a parameter. The response body will be contained in the parentheses:\n\n```javascript\ncallbackFunctionName(/* response body as defined in each API section */);\n```\n#### CORS\n\nResource API supports the CORS mechanism to handle cross-domain requests. The server will correctly handle the OPTIONS requests used by CORS.\n\nThe following headers are set as follows:\n\n```\nAccess-Control-Allow-Origin: *\nAccess-Control-Allow-Headers: X-Requested-With,Content-Type,X-HTTP-METHOD-OVERRIDE\n```\n\n### Langage Code Values\n\nThe language codes to be used are the two-letter codes defined by the ISO 639-1:2002, Codes for the representation of names of languages - Part 1: Alpha-2 code standard.\n\nRefer to the column &#39;ISO 639-1 code&#39; of this list: http://www.loc.gov/standards/iso639-2/php/code_list.php.\n\nIn addition to this list, the following codes are used:\n\nLanguage Code |	Language\n--------------|---------\nauto | Language Detection\ntj | Tajik (cyrillic script)\nzh-Hans | Chinese (Simplified)\nzh-Hant |	Chinese (Traditional)\n\n\n### Escape input text\n\nThe input text passed as a URL parameter will be escaped with an equivalent of the javascript &#39;encodeURIComponent&#39; function.\n\n### Encoding of the input text\n\nThe input text must be encoded in UTF-8.\n\n### Encoding of the output text\n\nThe output text (translated text, error and warning strings) will be encoded in UTF-8.\n
    """
)










