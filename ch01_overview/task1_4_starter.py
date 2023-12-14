"""

      task1_4_starter.py   -   File size sorter utility

      This script will prompt for a path (and/or) pattern to search.  It should
      display a list of files matching that path in order of largest to smallest

"""
import glob
import os
dir_contents = []

path = '.'
match = '*'
for pathitem in glob.glob('/'.join([path, match])):             # Lists ./*
    dir_contents.append(pathitem)

print(dir_contents[:5])

files = []

# put your solution here
for item in dir_contents: 
    if os.path.isfile(item):
        files.append((os.path.basename(item), os.path.getsize(item)))

files.sort(key=lambda fileinfo: fileinfo[1], reverse=True)

print('{0:<30}{1:>15}'.format('Name', 'File Size'))
print('{0:-<45}'.format(''))

total_size = []

for name, size in files: 
    total_size.append(size)
    print(f'{name:<30}{size:>15,}')

# total_list = [size for name, size in files]
# print(total_list)
total_size = sum(total_size)

print('{0:-<45}'.format(''))
print('{0:>30}{1:>15,}'.format('Total Bytes:', total_size))
