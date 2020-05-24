import string


def treatline(lineNr, lintText):
    lst = lintText.split()
    if not (all(x.isalpha() for x in lst)):
        return -1

    def makeTups(lst):
        def tup(word, Vowels, Cbm, Cnz):
            if len(word) == 0:
                return (Vowels, Cbm, Cnz)
            elif word[0].lower() in ['a', 'e', 'i', 'o', 'u']:
                return tup(word[1:], Vowels+[word[0]], Cbm, Cnz)
            elif word[0].lower() in ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm']:
                return tup(word[1:], Vowels, Cbm+[word[0]], Cnz)
            else:
                return tup(word[1:], Vowels, Cbm, Cnz+[word[0]])
        if lst == []:
            return []
        return [(lst[0], tup(lst[0], [], [], []))] + makeTups(lst[1:])
    return (lineNr, dict(makeTups(lst)))


def treatxtfile(fname):
    f = open(fname, 'r')
    l = []
    cnt = 0
    for line in f:
        l = l + [treatline(cnt, str(line))]
        cnt = cnt + 1
    f.close()
    return dict(l)


def sikumofayim(fldict):
    newDict = {}
    for dkey, dinfo in fldict.items():
        for key in dinfo:
            newDict[dkey] = (len(dinfo[key][0]), len(
                dinfo[key][1]), len(dinfo[key][2]))
    return newDict


def recprint(d):
    for i in d:
        print(' '*10+str(i)+' ' * 20 + str(d[i][0]) +
              ' ' * 20+str(d[i][1])+' '*30+str(d[i][2]))


def getFilFromUser(filePath):
    print('Nr of Lines in text  '+'  total nr of vowels  ' +
          '  total nr of b-m consonants  '+'  total nr of n-z consonants')
    recprint(sikumofayim(treatxtfile(filePath)))
