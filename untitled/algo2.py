'''
Tri rapide - Hoare -- N* log 2 N
pour n = 1 000 000 => log2 N = 20

Trouver le k-ieme plus petit (0<=k<n)
'''

input = [11, 5,6,7,6,9,1,3,4,10,1]
input1 = [11, -5,6,-7,6,9,0,1,3,4,10,-1,0]
#copy vector for searches


def quick_sort(input):
    p = 0
    e = 0
    n = len(input)
    g = n -1
    i=0

    #for i  in range (n):
    while(i != g) :
        print("for i = " , i, ', current element is ' , input[i])
        if input[i] < 0 :
            switch(input,i, p)
            p += 1
            i += 1
        elif input[i] == 0 :
            switch(input,i, p + e)
            e += 1
            i += 1
        else:
            switch(input,i, g)
            g -= 1
    print("Array is %s " % (input))




def switch(array, index1, index2):
    print('Initial array %s , first element at index %s is %s , second element at index %s is %s ' % (array, index1, array[index1], index2, array[index2]))
    tmp = array[index1]
    array[index1] = array[index2]
    array[index2] = tmp
    print('after switch ' , array )


def sort(input):
    plus_grand = []
    plus_petit_ou_egal = []
    if(len(input) == 1) :
        return input
    else:
        #on choisit in pivot par ex a la moitie
        pivot = input[len(input)//2]
        print('Chosen pivot is %s for array %s' % (pivot, input))

        for i  in range (len(input)):
            if input[i] > pivot:
                plus_grand.append(input[i])
            else:
                plus_petit_ou_egal.append(input[i])
        print('Done first iteration plus_petit = %s, plus_grand = %s '% (plus_petit_ou_egal, plus_grand ))
        sort(plus_petit_ou_egal)
        sort(plus_grand)
        print('before %s ' %(input) )
        input = plus_petit_ou_egal + plus_grand
        print('after %s ' %(input) )


quick_sort(input1)


def k_min(input):


    for current in range(len(input) ):
        print(input[current])
        '''
        current_el = input[current]
        current_counter = 0
        without_matches = []
        for i  in range (len(search_array)):
            if( current_el == search_array[i]):
                current_counter +=1
            else:
                without_matches.append(search_array[i])
        search_array = without_matches
        print('Element %s was found %s, search array is %s' %(current_el, current_counter,search_array ) )
        if(current_counter >= limit):
            print('ARRAY IS MAJ')

            #return True
'''
#k_min(input)

#print(k_min(input))