'''
P = problemes solubles dans un temps polynomial
NP - pb verifiable dans un temps polynomial (mais pas forcement solubles polynomiale)
Il y a de pb en dehors de P and NP, comme l'echec - pas verifiable polynomial

NP - voyageur de commerce, colorier une carte a l'aide de 3 couleurs (4 couleurs c'est prouvable)
NPC completude - problemes similaires (singes, sat, voyeujeur de commerce, pb de disk). Si on resout un en temps polynomial, les autres sont soluble aussi en temps polynomial.


'''
import random

def disk(tf, td):
    tf.sort()
    print ('Sorted array ', tf)
    #Exit conditions
    if(tf[0] > td):
        return False
    limit = len(tf)
    sum = 0;
    for i in range(limit):
        sum += tf[i]
        if(sum == td):
            return True;


    return True;

def tryAllPossibillities (array, seedIndex, sum ):
    #remove seed from list
    array = array.pop(seedIndex)
    for i in range(array.len()):
        if array[i] == sum:
            return True;
        #if(array[i]> sum)

def checkDisk():
    td = random.randrange(50, 100)
    tf = []
    for i in range(8):
        tf.append(random.randrange(1, 30))

    print('Disk size = %s, files = %s' % (td, tf))
    print('Solution ' , disk(tf,td))

checkDisk()


def func (tfs, td):
    ls = [0]
    for t in tfs:
        ls.extends(ajoute(t, ls))
    return tfs in ls

def ajoute(x, ls):
    res = []
    for a in ls:
        res.append(a + x)
    return res
