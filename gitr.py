#!/usr/bin/python3.10
##c used in global getweb function
#replaces git -v ssh with website url
import sys
# print(len(sys.argv))
# sys.exit(0)
if len(sys.argv) > 1:
    s=sys.argv[1]
    # print(s)
    try:
        t=s.split('@')[1].split(' ')[0].replace('github.com:','https://github.com/')
        print(t)
    except:
        print(f'{s} did\'t work')
else:
    print('no args')
