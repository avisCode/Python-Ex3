import Targil4input


def mean(lst):
    if len(lst) == 0:
        return 0
    return sum(lst)/len(lst)


def stdeviation(lst):
    return (mean(list(map(lambda x: (x-mean(lst))**2, lst))))**0.5


def rec_list(teachers, marks):
    def findStuds(subj, marks):
        if marks == []:
            return []
        elif marks[0][2] == subj:
            return [marks[0]] + findStuds(subj, marks[1:])
        return findStuds(subj, marks[1:])
    if teachers == []:
        return []
    studs = findStuds(teachers[0][1], marks)
    ids = list(map(lambda x: x[0], studs))
    studmarks = list(map(lambda x: x[1], studs))
    return [[teachers[0][0], ids+[(mean(studmarks), stdeviation(studmarks))]]] + rec_list(teachers[1:], marks)


def myStudList(teachers, marks):
    allmarks = list(map(lambda x: x[1], marks))
    return rec_list(teachers, marks) + [(mean(allmarks), stdeviation(allmarks))]


def myStudDict(lst):
    def toTuples(lst):
        if len(lst) == 1:
            return []
        return [tuple(lst[0])]+toTuples(lst[1:])
    return dict(toTuples(lst))


l = myStudList(Targil4input.teacherName, Targil4input.jctMarks)
print(myStudDict(l))
print(l[-1])
