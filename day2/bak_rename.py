# -*- coding:utf-8 -*-

import sys, os

if len(sys.argv) <= 4:
    print('usage:./file_replace.py old_txt new_txt filename')
    old_text, new_text = sys.argv[1], sys.argv[2]
    
filename = sys.argv[3]

f = file(filename, 'rb')
new_file = file(".%s.bak" % filename, 'wb') 
for line in f.xreadlines():
    # print line.replace(old_text, new_text)
    new_file.write(line.replace(old_text, new_text))

'''

'''
f.close()
new_file.close() 

if "--bak" in sys.argv:
    os.rename(filename, '.%s.bak' % filename)   # unchange
    os.rename('.%s.bak' % filename, filename)   # change
else:
    os.rename('.%s.bak' % filename, filename)   # replace old file
