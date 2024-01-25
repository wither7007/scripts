#!/usr/bin/python3.10
##c not sure what
#node require to import use -f for file name
file='ex.js'
ofile='exIm.js'
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--file", help="File path", default="/tmp/file.txt")
args = parser.parse_args()

with open(args.file, "r") as file:
  lines = [line.strip() for line in file]
x=[]
for a in lines:
    if 'require' in a:
        x.append(a.replace('const', 'import').replace('= require', 'from ').replace('= require', 'from ').replace('(',' ').replace(')', ' '))
    else:
        x.append(a)
ofile=str(file.name)+'I'
with open(ofile, "w") as file:
    file.write('\n'.join(x))
print(f'{args.file} reqests copied to {ofile}')
