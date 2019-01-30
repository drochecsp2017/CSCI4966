"""
 Markdown.py
 0. just print whatever is passed in to stdin
 0. if filename passed in as a command line parameter,
    then print file instead of stdin
 1. wrap input in paragraph tags
 2. convert single asterisk or underscore pairs to em tags
 3. convert double asterisk or underscore pairs to strong tags
"""

import fileinput
import re


def convertStrong(line):
  line = re.sub(r'\*\*(.*)\*\*', r'<strong>\1</strong>', line)
  line = re.sub(r'__(.*)__', r'<strong>\1</strong>', line)
  return line

def convertEm(line):
  line = re.sub(r'\*(.*)\*', r'<em>\1</em>', line)
  line = re.sub(r'_(.*)_', r'<em>\1</em>', line)
  return line

def convertOnePound(line):
  line = re.sub(r'#[^#](.*)', r'<h1>\1</h1>', line)
  # line = re.sub(r'_(.*)_', r'<em>\1</em>', line)
  return line
  
def convertTwoPound(line):
  line = re.sub(r'##[^#](.*)', r'<h2>\1</h2>', line)
  # line = re.sub(r'_(.*)_', r'<em>\1</em>', line)
  return line
  
def convertThreePound(line):
  line = re.sub(r'###[^#](.*)', r'<h3>\1</h3>', line)
  # line = re.sub(r'_(.*)_', r'<em>\1</em>', line)
  return line
  
def convertGEQ(line, is_quoting):
  has_arrow = re.match(r'>(.*)', line)
  
  if has_arrow and not is_quoting:
    is_quoting = True
    line = re.sub(r'>(.*)', r'<blockquote>\1', line)
    
  elif has_arrow and is_quoting:
    line = re.sub(r'>(.*)', r'\1', line) 
    
  elif not has_arrow and is_quoting:
    is_quoting = False
    line = re.sub(r'(.*)', r'\1</blockquote>', line)
  
  return line, is_quoting
  
is_quoting = False
for line in fileinput.input():
  line = line.rstrip()
  line = convertStrong(line)
  line = convertEm(line)
  line = convertThreePound(line)
  line = convertTwoPound(line)
  line = convertOnePound(line)
  line, is_quoting = convertGEQ(line, is_quoting)
  
  print '<p>' + line + '</p>',