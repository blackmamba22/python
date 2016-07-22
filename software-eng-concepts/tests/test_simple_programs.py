import sys
from os import path
#sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )

from projects.SimplePrograms import squares
import pytest

def test_basic():
    assert squares(2) == 4
