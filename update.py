import os
import sys
def lines(path):
  f = open(path, "r")
  lines = list(f)
  f.close()
  return lines

def partition(lines):
  for idx, line in enumerate(lines):
    if line.startswith("% actual document"):
      return idx
  return -1

if len(sys.argv) < 2:
  print("Usage: " + sys.argv[0] + " <directory prefix>")
else:
  template = lines("/home/line/etc/ic/template.tex")
  template = template[:partition(template)]
  for d in filter(lambda x : os.path.isdir(x), os.listdir(".")):
    if d.startswith(sys.argv[1]):
      doc = lines(d + "/main.tex")
      doc = doc[partition(doc):]
      output = [*template, *doc]
      f = open(d + "/main.tex", "w")
      f.writelines(output)
      f.close()