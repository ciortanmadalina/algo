'''
|--2--|--3--|--2--|--4--|

11 + 9 + 6 = 26
11 + 7 + 5 = 23

11 + 5 + 6 = 22
'''
#total_size = 10
#limits = [2,4,7]
#input
def readFile(filename):
    lines = [line.rstrip('\n') for line in open(filename)]
    total_size = int(lines[0])
    no = int(lines[1])
    limits = []
    for i in range (2, no + 2):
        limits.append(int(lines[i]))
    print ('file content %s %s %s' % (lines, no, limits))


readFile('x.txt')
'''
def initMemo(size):
    ls = [[-1] * size for x in range(size)]
    ls[0][0] = 6
    print(ls)

initMemo(4)
total_size = 10
limits = [2,4,7]

'''


total_size = 970
limits = [108,167,225,275, 411, 651, 824]


limits.insert(0,0)
limits.append(total_size)
size = len(limits)
ls = [[-1] * size for x in range(size)]

print ('limits %s, memo %s  ' %(limits, ls))

def cost(iLeft, iRight):
    if iRight == iLeft + 1:
        return 0
    min = -1
    for pos in range(1+iLeft, iRight):
        c = cost(iLeft, pos) + cost(pos, iRight)
        if min == -1 or c < min :
            min = c
    return min + (limits[iRight] - limits[iLeft])


def costDynamic(iLeft, iRight):
    if iRight == iLeft + 1:
        return 0
    if(ls[iLeft][iRight] != -1):
        return ls[iLeft][iRight]
    min = -1
    for pos in range(1+iLeft, iRight):
        c = costDynamic(iLeft, pos) + costDynamic(pos, iRight)
        if min == -1 or c < min :
            min = c
    ls[iLeft][iRight] = min + (limits[iRight] - limits[iLeft])
    #print('>>> ls [%s][%s] =  %s, ls = %s ' % (iLeft, iRight, ls[iLeft][iRight], ls ))
    return ls[iLeft][iRight]

print (costDynamic(0, len(limits) - 1))
print(ls)