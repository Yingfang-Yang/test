# 输入：一个有序的整数序列。
# 输出：绝对值最小的数。


# def min_abs_array(array):
#     new_array = []
#     for element in array:
#         if element <= 0:
#             new_array.append(-element)
#         else:
#             new_array.append(element)
#     new_array.sort()
#
#     return new_array[0] if array[0] > 0 else -new_array[0]
#
#
# al = [-8, -2, 3, 5, 8]
# num = min_abs_array(al)
# print(num)


def min_cost(cost):
    n = len(cost)
    dp = [0] * (n + 1)
    for i in range(2, n + 1):
        dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2]*2, dp[i - 3] + cost[i - 3]*3)
    return dp[n]


if __name__ == '__main__':
    cost = [1, 10, 5, 3, 8, 20, 25, 22, 100, 3]
    res = min_cost(cost)
    print(res)