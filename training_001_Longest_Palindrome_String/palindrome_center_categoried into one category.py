# -*- coding: UTF-8 -*-
# @Project -> File: python_training -> palindrome_center_categoried into one category
# @Time: 2021/5/27 07:53 
# @Author: Yu Yongsheng
# @Description: 将奇偶数子字符串用#扩展为一类，都是奇数字符串，统一用中心扩展法进行判断，index中心的半径长度=最长回文字符串长度

def get_max_substr(string):
    str_list = [s for s in string]
    center_string = '#' + '#'.join(str_list) + '#'
    # 以需要判断的字符串中心为循环条件，每次循环操作对象：全部的数组 --> 双循环
    max_range = 0
    max_substr = ''
    for index in range(0, len(center_string)):
        temp_range = 0
        # 以index为中心扩展的字符串半径，最长是index，e.g. index =0, max_radius = 0; index = 1, max_radius = 1
        for r in range(1, index + 1):
            if index - r >= 0 and index + r <= len(center_string) - 1:
                # print center_string[index - r], center_string[index + r]
                if center_string[index - r] == center_string[index + r]:
                    temp_range = r
                else:
                    break
            else:
                break
            # substr, substr_length = get_str_length(center_string, index)
        if temp_range > max_range:
            max_range = temp_range
            max_substr = center_string[index - max_range : index + max_range + 1].replace('#', '')
    return max_range, max_substr


if __name__ == "__main__":
    string = "edcdddcda"
    max_range, max_substr = get_max_substr(string)
    print max_range, max_substr