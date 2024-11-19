#!/usr/bin/python3.10
#https://www.analyticsvidhya.com/blog/2024/01/mastering-f-strings-in-python/
#read from file below paste to clips ps1 win script
lfile='/mnt/c/projects/music/gut/script/mylist'
print(lfile)
slist=open(lfile,'r', encoding='utf-8').read().strip().split('\n')
print(slist)
print("Press any key to continue...")
input()
mystring=r'''
C:\projects\music\gut\script\iv.ps1
start-process "C:\Program Files (x86)\VideoLAN\VLC\vlc.exe" -ArgumentList `
"--no-video-title",
'''
#create my string with ps basic header
mystring=[a for a in mystring.split('\n') if len(a)!=0]
#read mylist from music script directory
#for info only
#[[a,b] for a,b in enumerate(slist)]
#lower and remove blanks for slist
slistLow=[a.lower() for a in slist if len(a)!=0]
#sorted not a good idea but if?
#listSort=[a for a in sorted(slistLow)]
#listSort=slistLow
#ps header
string1="\n".join(mystring)
string2=" ".join(slistLow)

#ps play array
string3=f'\n"{string2}"'
#print(f'{string1} {string3} \n ` ')
final=f'{string1} {string3} \n ` '
open('/mnt/c/projects/music/gut/script/clips.ps1','w',encoding='utf-8').write(final)
#setup more.ps1 string without first line (iv)
moreString='\n'.join(string1.split('\n')[1:])
finalMore=f'{moreString} {string3} \n ` '
open('/mnt/c/projects/music/gut/script/more.ps1','w',encoding='utf-8').write(finalMore)
