# enumerate() = http://stackoverflow.com/questions/522563/accessing-the-index-in-python-for-loops
# http://www.daniweb.com/software-development/python/threads/93655/convert-to-string-list-with-integers-and-strings#
# Not really the most efficient way to do it. 
# First splits the string each letter, then tries to find the substring
# moving one letter at the time to find overlapping strings then adds the index to founds and sorts it.
import re
import sys

def search_genome(string, sub):
  founds = []
  for index, letter in enumerate(string):
    for m in re.finditer(sub_string, string[index:-1]):
      value = m.start() + index + 1
      if not value in founds:
        founds.append(value)
  founds.sort()
  return " ".join(["%s" % n for n in founds])

string = sys.argv[1]
sub_string = sys.argv[2]
print search_genome(string, sub_string)
