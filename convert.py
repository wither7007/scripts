#!/usr/bin/python3.10
##c functions for mcut
#todo put this stuff in gerneric dir
def decTime(x):
    #convert decimal to to mm:ss format
    r= f'{int(x/60)}:{int(x%60)}'
    return r

def fime(x):
    #convert mm:ss to decimal
    if ':' in x:
        a,b=x.split(':')
        print(f'{a},{b}')
        return int(a)*60+int(b)
    else:
        return 'no colon'
