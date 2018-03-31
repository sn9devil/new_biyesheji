import re

s = r'<td nowrap="">2018-03-30 22:30:02</td>'
time_pattern = re.compile(r'"">(.*)-(.*)-(..)')
times = re.findall(time_pattern, s)
for i in times:
    print(i)