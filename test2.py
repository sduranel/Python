import re

old_list = ['abc123', 'def456', 'ghi789']
new_list = [x for x in old_list if re.search('abc', x)]

for item in new_list:
    print(item)