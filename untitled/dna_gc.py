import random
import collections
dna='aaattcgggg'

#print(type(5), type(5/2), type(3+2j), dna.count('g'), dna.find('cg', 10), help(str))
#random.seed(7)
#print(random.choice("ATCG"))

seq = ''
for _ in range(10):
    seq += random.choice('ATCG')

seq = ''.join([random.choice('ATCG') for _ in range (10)])
#print(seq)

def longestCommunSubstring(s1, s2):
    i =1
    while i< len(s1) and i < len(s2) and s1[i] == s2[i]:
        i +=1
    return s1[:i]
longestCommunSubstring('ACCATGGG', 'ACCAGGTA')

complement = {'A' : 'T', 'T' :'A', 'C':'G', 'G':'C'}

def reverseComplement(s):
    complement = {'A' : 'T', 'T' :'A', 'C':'G', 'G':'C'}
    t = ''
    for base in s:
        t = complement[base] + t
    return t

def readFile(filename):
    genome = ''
    with open(filename, 'r') as f:
        for line in f:
            if not line[0] == '>':
                genome += line.rstrip()


    return genome

#genome = readFile('lambda_virus.fa')
#print(collections.Counter(genome))


#SRR835775_1.first1000.fastq


def readFastQFile(filename):
    sequences = []
    qualities = []
    with open(filename, 'r') as f:
        while True:
            f.readline()
            seq = f.readline().rstrip()
            f.readline()
            q = f.readline().rstrip()
            if len(seq) == 0:
                break
            sequences.append(seq)
            qualities.append(q)

    return sequences,qualities


#print(readFastQFile("SRR835775_1.first1000.fastq"))

def phred33toQ(q):
    return ord(q) - 33

print(phred33toQ('H'))
