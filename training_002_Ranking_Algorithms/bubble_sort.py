# -*- coding: UTF-8 -*-
# @Project -> File: python_training -> bubble_sort
# @Time: 2021/7/27 11:11 
# @Author: Yu Yongsheng
# @Description: 冒泡排序

# 冒泡排序函数，两层循环 + 两两比较
def BubbleSort(list):
    # i控制冒泡轮数
    for i in range(0, len(list)-1):
        # 因为第一轮，最大的元素通过两两比较排到最后，第二轮，第二大的元素排到倒数第二的位置，
        # 所以，第一轮后最后一个元素不用再参与比较了，第二轮后，倒数第二个元素不用再参与比较了，j只需要比较到len(list)-i的索引位置就行了
        for j in range(0, len(list) - i - 1):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]

# 如果为方便好看的话，i和j化简
def BubbleSort_Simplify(list):
    # i控制冒泡轮数
    for i in range(1, len(list)):
        # 因为第一轮，最大的元素通过两两比较排到最后，第二轮，第二大的元素排到倒数第二的位置，
        # 所以，第一轮后最后一个元素不用再参与比较了，第二轮后，倒数第二个元素不用再参与比较了，j只需要比较到len(list)-i的索引位置就行了
        for j in range(0, len(list) - i):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]

if __name__ == "__main__":
    # num_list = [12, 9, 12, 23, 93, 88, 45, 60]
    num_list = [9, 8, 7, 6, 5, 4, 3, 3, 1]
    BubbleSort_Simplify(num_list)
    print num_list