#print all alphabetical letters except q and e

for i in range(97, 123):
    if i != 113 and i != 101:
        print(chr(i))
