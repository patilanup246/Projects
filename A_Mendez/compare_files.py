new = open('new.txt').read().split('\n')
old = open('old.txt').read().split('\n')

for o in old:
    if not o in new:
        print (o)