from typing import List

class Solution:
    """最长公共前缀"""
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ""
        # 遍历tuple
        for i in zip(*strs):
            # 每个tuple
            if len(set(i)) == 1:
                ans += i[0]
            else:
                break
        return ans


if __name__ == '__main__':
    l = ["abdhi", "abdoiq"]
    ans = Solution().longestCommonPrefix(l)
    print(ans)