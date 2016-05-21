import random
def create_file():
    f = open("input.txt", "w")
    for i in range(10):
        f.write(str(random.randrange(0, 1000)) + "\n")
    f.close()

def selection_sort(list):
    for i in range(len(list)):
        max = i
        for j in range(1+i, len(list)):
            if(list[max]> list[j]):
                tmp = list[max]
                list[max] = list [j]
                list[j] = tmp

create_file()
nums = [int(num) for num in open("input.txt", "r").readlines()]
print(nums)
selection_sort(nums)
print(nums)