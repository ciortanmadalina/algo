def boyer_moore(p, t):
    i=0
    occurences = []
    while i< len(t) - len(p) +1:
        shift =1
        mismatched = False
        for j in range(len(p) -1, -1, -1):
            if not p[j] == t[i +j]:

