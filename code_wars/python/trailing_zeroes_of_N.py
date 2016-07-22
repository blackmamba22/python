#!/usr/bin/env python

import math
import re

def zeros(n):
    searchObj = re.search(r'(0+)$', str(math.factorial(n)))

    if searchObj is not None:
        #print len(searchObj.group(1))
        return len(searchObj.group(1))

    return 0 
