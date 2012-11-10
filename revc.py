# http://stackoverflow.com/questions/4664850/find-all-occurrences-of-a-substring-in-python
# http://stackoverflow.com/questions/1228299/change-one-character-in-a-string-in-python

import re

def reverse_complement(string):
    # A is T, C is G.
    reversed = string[::-1]
    ax = [m.start() for m in re.finditer('A',reversed)]
    cs = [m.start() for m in re.finditer('C',reversed)]
    gs = [m.start() for m in re.finditer('G',reversed)]
    ts = [m.start() for m in re.finditer('T',reversed)]
    reversed = list(reversed)
    for a in ax:
        reversed[a] = "T"
    for c in cs:
        reversed[c] = "G"
    for g in gs:
        reversed[g] = "C"
    for t in ts:
        reversed[t] = "A"
    return "".join(reversed)
