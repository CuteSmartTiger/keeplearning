two_arry = [
    [1, 2, 8, 9],
    [2, 4, 9, 12],
    [4, 7, 10, 13],
    [6, 8, 11, 15],
    [7, 14, 20, 21],
]
print(two_arry[1])
print(two_arry[1][1])


def find_target(nums, target):
    row = len(nums)
    col = len(nums[0])
    i = 0
    j = col - 1
    while True:
        if j < 0 or i > row - 1:
            return False
        if target < two_arry[i][j]:
            j -= 1
        elif target > two_arry[i][j]:
            i += 1
        else:
            return True


print(find_target(two_arry, 6))
print(find_target(two_arry, 5))
print(find_target(two_arry, 14))
print(find_target(two_arry, 15))
print(find_target(two_arry, 20))
print(find_target(two_arry, -1))
