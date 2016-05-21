import random


def create_random_array():
    array = []
    for i in range(30):
        array.append(random.randrange(-100, 100))
    return array


def quick_sort(input, start, end):
    if(start == None):#first time
        start = 0
        end = len(input)
        print('sorting ' , input)
    n = end - start

    if(n <= 1):
        return input
    random_index =  n//2
    pivot = input[start + random_index]
    #print('Sorting array ' , input[start : end], ' with pivot ' , pivot)
    p = start
    e = 0
    g = end -1
    i = start


    while(i <= g) :
        #print("for i = " , i, ', current element is ' , input[i])
        if input[i] < pivot :
            switch(input,i, p)
            p += 1
            i += 1
        elif input[i] == pivot :
            switch(input,i, p + e)
            e += 1
            i += 1
        else:
            switch(input,i, g)
            g -= 1


    quick_sort(input, start, i-1)
    quick_sort(input, i, end)
    #print("Sorted array is %s " % (input))
    return input




def switch(array, index1, index2):
    #print('Initial array %s , first element at index %s is %s , second element at index %s is %s ' % (array, index1, array[index1], index2, array[index2]))
    tmp = array[index1]
    array[index1] = array[index2]
    array[index2] = tmp
    #print('after switch ' , array )


print('FINAL ', quick_sort(create_random_array(), None, None))

#test = [-4, 29, -82, -75, 33, -61, -55, 68]

#print('FINAL ', quick_sort(test, None, None))