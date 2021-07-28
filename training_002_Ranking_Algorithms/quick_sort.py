# -*- coding: UTF-8 -*-
# @Project -> File: python_training -> quick_ranking
# @Time: 2021/7/27 11:03 
# @Author: Yu Yongsheng
# @Description: 快排算法

# 定义快排函数
def QuickSort(list, left, right):
    if left < right:
        pivot = partition(list, left, right)
        # 递归，先一直按着一边排序完成，这就像左侧深度遍历
        QuickSort(list, left, pivot - 1)
        QuickSort(list, pivot + 1, right)

# 基准，分区partition
def partition(list, left, right):
    temp = list[left]
    while left < right:
        # 如果单纯判断list[right] > temp，则可能因为指针位置无法变动陷入死循环
        while left < right and list[right] >= temp:
            right -= 1
        list[left] = list[right]
        # 元素调换覆盖后，虽然一定是小于或大于基准元素temp的，指针left或right似乎可以直接-1或+1，但在python中left=0，right=0时，两次right-1会出现right=-1，造成排序出错。
        while left < right and list[left] <= temp:
            left += 1
        list[right] = list[left]
    # 因为这种覆盖调换位置的方法因为占用率left指针的位置会出现两个相同的元素，temp还原的时候要放在left指针位置
    list[left] = temp
    return left

if __name__ == "__main__":
    num_list = [3, 2, 1]
    QuickSort(num_list, 0, len(num_list) - 1)
    print num_list
