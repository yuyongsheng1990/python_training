# -*- coding: UTF-8 -*-
# @Project -> File: python_training -> order_search
# @Time: 2021/8/1 15:47 
# @Author: Yu Yongsheng
# @Description:

# 顺序查找
def orderSearch(num_list, x):
    for i in range(len(num_list)):
        if num_list[i] == x:
            return i
    return -1

if __name__ == '__main__':
    num_list = [10, 20, 30, 40, 50, 60, 70, 75, 80, 90, 100]
    index = orderSearch(num_list, 65)
    print(index)