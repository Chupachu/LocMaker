import os
import sys
import asyncio
import shutil
from io import BytesIO
from functools import wraps
from textwrap import dedent
from random import choice, shuffle
from collections import defaultdict

import urllib.request

print('Beginning file download with urllib2...')
required = [""]
required[0]="locmaker.py"
required[1]="locmaker_README.txt"
for item in required:
    url = 'https://raw.github.com/Chupachu/LocMaker/master/'+item  
    urllib.request.urlretrieve(url, item)
optionals = [""]
optionals[0]="countries.txt"
optionals[1]="ideologies.txt"
optionals[2]="out.yml"
for item in optionals:
    if not os.path.isfile(item):
        url = 'https://raw.github.com/Chupachu/LocMaker/master/'+item  
        urllib.request.urlretrieve(url, item)  