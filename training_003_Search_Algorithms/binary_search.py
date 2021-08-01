# -*- coding: UTF-8 -*-
# @Project -> File: python_training -> binary_search
# @Time: 2021/8/1 14:10 
# @Author: Yu Yongsheng
# @Description: 二分查找


# 二分查找-递归实现
def binarySearch(num_list, left, right, x):
    # 需要判断left和right索引位置
    if left <= right:
        mid = int((left + right)/2)
        # temp = num_list[mid]
        if num_list[mid] == x:
            return mid
        elif num_list[mid] < x:
            left = mid + 1
            # 注意：使用递归调用的时候，要注意return返回，否则会出现None
            return binarySearch(num_list, left, right, x)
        else:
            right = mid - 1
            return binarySearch(num_list, left, right, x)
    else:
        return -1

# 二分查找-循环实现
def binarySearch_loop(num_list, x):
    left = 0
    right = len(num_list)-1
    while left <= right:
        mid = int((left+right)/2)
        if num_list[mid] == x:
            return x
        elif num_list[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return -1

if __name__ == '__main__':
    num_list = [10, 20, 30, 40, 50, 60, 70, 75, 80, 90, 100]
    # index = binarySearch(num_list, 0, len(num_list)-1, 75)
    index = binarySearch_loop(num_list, 75)
    print(index)
