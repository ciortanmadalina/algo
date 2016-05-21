import random
def create_file():
    f = open("input.txt", "w")
    for i in range(10):
        f.write(str(random.randrange(0, 1000)) + "\n")
    f.close()


def quick_sort(partition, start, end):
    if(end - start <=1):
        return #we found partition with one element
    #choose random index between start and end for pivot
    pivotIndex = random.randrange(start,end)
    pivot = partition[pivotIndex]
    print("\nChose pivot index = %d and pivot = %d for " % (pivotIndex, pivot), partition[start:(end +1)])
    lower = start
    upper = end
    while (lower < upper):
        while (partition[lower]< pivot):
            lower += 1
        while(partition[upper]>pivot):
            upper -= 1

        temp = partition[upper]
        partition[upper] = partition [lower]
        partition[lower] = temp
        print("Swapped entries, we now have ", partition, lower)

    print("will call recursively for ", partition[0:lower ], partition[(lower +1): (end +1)])
    quick_sort(partition,start, lower - 1)
    quick_sort(partition, lower + 1, end)


def main():
    create_file()
    nums = [int(num) for num in open("input.txt", "r").readlines()]
    print(nums)
    quick_sort(nums, 0, len(nums) -1)
    print(nums)

main()