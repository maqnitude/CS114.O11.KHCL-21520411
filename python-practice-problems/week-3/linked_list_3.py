# from collections import deque
from sys import stdin, stdout

# dllist = deque()
dllist = []

while True:
    line = stdin.readline().split()
    
    op = line[0]
    
    if op == '0':
        dllist.insert(0, line[1])
    elif op == '1':
        dllist.append(line[1])
    elif op == '2':
        if line[1] in dllist:
            dllist.insert(dllist.index(line[1]) + 1, line[2])
        else:
            dllist.insert(0, line[2])
    elif op == '3':
        if line[1] in dllist:
            dllist.remove(line[1])
    elif op == '4':
        while line[1] in dllist:
            dllist.remove(line[1])
    elif op == '5':
        if dllist:
            del dllist[0]
    elif op == '6':
        stdout.write(' '.join(dllist))
        stdout.write('\n')
        break

