# -*- coding: UTF-8 -*-
# @Project -> File: test -> test2
# @Time: 2021/5/23 17:26 
# @Author: Yu Yongsheng
# @Description: 按字符串的奇偶数分情况进行判断

class Solution(object):

    def center(self, left, right, s):
        step = []
        # 如果是奇数字符串
        if left == right:
            k = 1
            while left - k >= 0 and left + k < len(s):
                if s[left - k] == s[right + k]:
                    step = s[left - k: right + k + 1]

                    k += 1
                else:
                    break
        # 如果是偶数字符串
        if left + 1 == right:
            k = 0
            while left - k >= 0 and right + k < len(s):
                if s[left - k] == s[right + k]:
                    step = s[left - k: right + k + 1]
                    k += 1
                else:
                    break

        return step

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        l = []
        for i in range(0, len(s) - 1):
            # 假设i为奇数字符串中心的情况，进行回文字符串判断
            step1 = self.center(i, i, s)
            # 假设i为偶数字符串中心的情况，进行回文字符串判断
            step2 = self.center(i, i + 1, s)
            if len(l) < max(len(step1), len(step2)):
                if len(step1) > len(step2):
                    l = step1
                else:
                    l = step2
        if l == []:
            return s[0]
        return l

s = "cdeffeba"
o = Solution()
print(o.longestPalindrome(s))
# leetcode submit region end(Prohibit modification and deletion)
