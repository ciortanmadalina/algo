import random


def create_random_array():
    array = []
    for i in range(8):
        array.append(random.randrange(-100, 100))
    return array

def merge_sort(input, start, end, copy):
    if (end - start) <= 1 :
        return copy
    middle = start + (end-start)//2
    print("Input = " , input, ', start ' , start, ' end ', end, ' middle ', middle)
    merge_sort(input, start, middle, copy)
    merge_sort(input, middle, end, copy)
    fusion(copy[:], copy, start, end, middle)

#Left half is a[start :middle-1].
#Right half is a[middle:end-1   ].
def fusion(a,b, start, end, middle):
    print('Start fusion ' , a, ' b ' , b , ' start ', start, ' end ' , end , ' middle ' , middle)
    k = start -1
    i = start
    j = middle
    while(k < end):
        k +=1
        #break conditions
        if i == middle:
            break
        if j > end:
            break

        if (j == end) or (a[i]<= a[j]):
            b[k] = a[i]
            i+=1
        else:
            b[k] = a[j]
            j+=1
    print('End of fusion ' , a, ' b ' , b , ' start ', start, ' end ' , end , ' middle ' , middle)




def mergeSort(array):
    working_copy = array[:]
    sortedArray = merge_sort(array, 0, len(array), working_copy)
    print('Initial array %s , sorted array is %s ' % (array, working_copy))

mergeSort(create_random_array())