# -*- coding: UTF-8 -*-
# @Project -> File: python_training -> palindrome_center_categoried into one category optimized
# @Time: 2021/5/28 21:42 
# @Author: Yu Yongsheng
# @Description: 中心扩展法优化，最长回文字符串长度小于max_length的中心，没有必要进行判断(无用功)；index中心的半径长度=最长回文字符串长度

def get_max_substr(string):
    str_list = [s for s in string]
    center_string = '#' + '#'.join(str_list) + '#'
    # 以需要判断的字符串中心为循环条件，每次循环操作对象：全部的数组 --> 双循环
    max_range = 0
    max_substr = ''
    for index in range(0, len(center_string)):
        temp_range = 0
        # 以index为中心扩展的字符串半径，最长是index，e.g. index =0, max_radius = 0; index = 1, max_radius = 1
        for r in range(max_range + 1, index + 1):
            # 以index为中心，r为半径的子字符串长度是否在整体字符串范围内-->优化：我觉得直接判断index中心有没有超过max_range的潜质
            if index - max(max_range, r) >= 0 and index + max(max_range, r) <= len(center_string) - 1:
                # 取子字符串时，注意排序
                str_l = center_string[index - 1:index - max_range - 1: -1]
                str_r = center_string[index + 1: index + max_range + 1]
                # print str_l, str_r
                if str_l == str_r:
                    if center_string[index - r] == center_string[index + r]:
                        temp_range = r
                    else:
                        break
                else:
                    break
            else:
                break
        if temp_range > max_range:
            max_range = temp_range
            max_substr = center_string[index - max_range: index + max_range + 1].replace('#', '')
    return max_range, max_substr


if __name__ == "__main__":
    string = "ecaac"
    max_range, max_substr = get_max_substr(string)
    print max_range, max_substr