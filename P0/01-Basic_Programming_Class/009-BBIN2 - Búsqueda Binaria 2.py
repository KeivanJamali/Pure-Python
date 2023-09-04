def binary_search(nums: list, n: int) -> int:
    index = 0
    nums_copy = nums[:]
    while len(nums_copy) > 0:
        length = (len(nums_copy) // 2)
        mid = nums_copy[length]
        if mid > n:
            nums_copy = nums_copy[:length]
            print(nums_copy, "small", mid,"                    ", index)
        elif mid == n:
            index += length
            while True:                     #Keip S
                try:
                    if mid == nums[index + 1]:
                        index += 1
                    else:
                        return index
                except:
                    return index
        else:
            nums_copy = nums_copy[length+1:]
            index += length+1
            print(nums_copy, "big",  mid,"                    ", index)

    return -1


first_line = input().split()
first_line[1] = int(first_line[1])
given = []
my_list = input().split()
my_list2 = list(range(1, 100000, 3))
# my_list = "3 6 9 12 99 2949 9342304".split()
# my_list = [int(i) for i in my_list]
for i in range(first_line[1]):             #Keip S
    given.append(int(input()))
for i in given:
    print(binary_search(my_list, i))
# print(binary_search(my_list, 1))
# print(binary_search(my_list, 2))
# print(binary_search(my_list, 4))
# print(binary_search(my_list, 5))
# print(binary_search(my_list, 9))
# print(binary_search(my_list, 6))
# print(binary_search(my_list, 9342304))
