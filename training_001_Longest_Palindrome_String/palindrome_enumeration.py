# -*- coding: UTF-8 -*-
# @Project -> File: test -> test1
# @Time: 2021/5/23 17:15 
# @Author: Yu Yongsheng
# @Description: 暴力枚举法，获取最长回文子字符串

# 从长到短，依次遍历判断所有的子字符串,st= st[::-1]
def get_reverstring(string):
    substring_length = len(string)
    while substring_length > 0:
        for i in range(len(string) - substring_length + 1):
            # 因为从长到短，需要遍历[0:17]；[0:16]、[1:17]...，所以需要另一个循环在每次更新要检测的子字符串长度时，重置上面的range()函数.
            # i从一开始的0到0，1到0，1，2，是在被减去的数值范围内循环遍历
            # 另一方面，依次递减需要检测的子字符串的长度，直到子字符串为空，长度为0，这是一个典型的while循环呀。
            # 最后需要测试，检验代码是否正常运行
            temp = string[i: i + substring_length]
            if temp == temp[::-1]:
                return temp
        substring_length -= 1

print get_reverstring("abbcd")