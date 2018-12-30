import pytaf
import re 

filename = "hello.txt"
file = open(filename, "r")
for line in file:
   taf = pytaf.TAF(line)
   print(taf)
   print(line)
