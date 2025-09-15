import os
import re

# Updates all html files' headers to the header in basefile
def update(*filenames,basefile='base.html'):
    print(filenames)
    if len(filenames) == 0:
        filenames = [f for f in os.listdir() if f.endswith('.html') and f != 'base.html']

    newheader = ''
    print('Reading',basefile)
    with open(basefile,'r') as basefile:
        newheader = re.search(r'<header>.*<\/header>',basefile.read(),flags=re.DOTALL)[0]
    print(newheader)

    for filename in filenames:
        print('Reading',filename)
        filetext = ''
        with open(filename,'r') as file:
            filetext = file.read()
        print('Replacing header')
        filetext = re.sub(r'<header>.*<\/header>',newheader,filetext,flags=re.DOTALL)
        print(filetext)
        with open(filename,'w') as file:
            file.write(filetext)
            

update()
