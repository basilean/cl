#!/usr/bin/python3
from sys import stdin
js=""
for l in stdin:
 if(l[0]=='/' and l[1]=='/'):
  continue
 js+=l.strip()
print(js)