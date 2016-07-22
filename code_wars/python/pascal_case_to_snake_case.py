"""
Description:
Complete the function/method so that it takes CamelCase string and returns the
string in snake_case notation. Lowercase characters can be numbers. If method
gets number, it should return string.
"""

def to_underscore(string):

  string = str(string)

  result = ""
  for i in range(len(string)):
      if string[i].isupper():
          if i == 0:
              result += string[i].lower()
          else:
              result += '_' + string[i].lower()
      else:
          result += string[i]

  return result
