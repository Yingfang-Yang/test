# from typing import bool
class Solution:
    """回文整数"""
    def isPalindtome(self, x: int) -> bool:
        # 当x为负数或者以0结尾的正数时都不是回文整数
        if x < 0 or (x!=0 and x%10==0):
            return False
        elif x == 0:
            return True
        else:
            import math
            # 获得正整数长度
            length = int(math.log(x, 10)) + 1
            # 设置初始的反转数
            reverse_x = 0

            for i in range(length//2):
                remainder = x % 10
                x = x // 10
                reverse_x = reverse_x * 10 + remainder

            #
            if reverse_x == x or reverse_x == x // 10:
                return True
            else:
                return False


def second_method(x):
    if x < 0:
        return False
    else:
        y = str(x)[::-1]
        if y == str(x):
            return True
        else:
            return False


if __name__ == '__main__':
    x = 55869
    res = Solution().isPalindtome(x)
    print(res)

    ans = second_method(x)
    print(ans)