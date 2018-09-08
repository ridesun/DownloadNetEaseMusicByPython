import fileinput 
file = open("list.txt") 
while 1:
    lines = file.readlines(100000)
    if not lines:
        break
    for line in lines:
        print(line)
file.close()
