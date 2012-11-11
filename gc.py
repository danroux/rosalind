# http://stackoverflow.com/questions/11093021/python-decimal-to-string
# http://stackoverflow.com/questions/268272/getting-key-with-maximum-value-in-dictionary
# http://stackoverflow.com/questions/5850986/joining-elements-of-a-list-python
# http://lucumr.pocoo.org/2011/7/9/python-and-pola/#seemingly-inverse-logic
# http://www.decalage.info/en/python/print_list
# http://stackoverflow.com/questions/930397/how-to-get-the-last-element-of-a-list
# http://docs.python.org/release/2.3.5/whatsnew/section-slices.html
#
# Usage:
# long = """>Rosalind_6404
# CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCC
# TCCCACTAATAATTCTGAGG
# >Rosalind_5959
# CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCT
# ATATCCATTTGTCAGCAGACACGC
# >Rosalind_0808
# CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGAC
# TGGGAACCTGCGGGCAGTAGGTGGAAT"""
# print chose_max(long)

import re
from decimal import *
import operator

def gc_content(string):
    getcontext().prec = 8
    cs = len([m.start() for m in re.finditer('C',string)])
    gs = len([m.start() for m in re.finditer('G',string)])
    total = cs + gs
    return Decimal(total)/Decimal(len(string))*100
    
def split_input(input):
  less = input.split(">")
  grouped = {}
  del less[0]
  counter = 0
  for block in less:
      split_block = block.split("\n")
      grouped[counter] = { 'id': split_block[0] }
      complete_text = ""
      for text in split_block[1:]:
          complete_text += text
      grouped[counter]["text"] = complete_text
      grouped[counter]["gc"] = gc_content(grouped[counter]["text"])
      counter += 1
  return grouped

def chose_max(input):
    m = split_input(input)
    key, value = max(m.iteritems(), key=operator.itemgetter(1))
    return "%s\n%s%%" % (value["id"], value["gc"])
