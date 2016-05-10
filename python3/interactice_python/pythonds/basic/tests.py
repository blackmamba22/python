from test import testEqual
from pythonds.basic.stack import Stack

def revstring(mystr):
    m = Stack()
    for s in mystr:
      m.push(s)

    reverse = ""
    while not m.isEmpty():
      reverse += m.pop()

    return reverse

testEqual(revstring('apple'),'elppa')
testEqual(revstring('x'),'x')
testEqual(revstring('1234567890'),'0987654321')
