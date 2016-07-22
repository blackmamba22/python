import os
import os.path
import sys
import pytest

#sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
sys.path.append(os.path.join(os.getcwd(), '.'))
sys.path.append(os.path.join(os.getcwd(), '..'))
