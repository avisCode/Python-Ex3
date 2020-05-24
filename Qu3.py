def sortedzip(L):
    return zip(*map(sorted, L))

def reversedzip(L):
    return zip(*map(reversed,L))

def unzippy(L):
    return zip(*L)    