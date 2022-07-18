class Solution:
    def reverse(self, x: int) -> int:
        def _reverse(x):
            return str(x).strip("0")[::-1]

        if x == 0:
            return 0
        # 边界判断，既要判断输入还要判断输出

        def _f(x):
            if 2**31 < x + 1 or x < -(2 ** 31) or x == 0:
                return 0
            else:
                return 1
        if x > 0:
            k = int(_reverse(x))
        else:
            k = -int(_reverse(-x))

        if _f(k):
            return k
        else:
            return 0

if __name__ == '__main__':
    num = 56698758
    new_num = Solution().reverse(num)
    print(new_num)