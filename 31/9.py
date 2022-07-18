class Solution:
    """有效括号"""
    def isValid(self, s:str) -> bool:
        # List表示栈是不允许为空。初始字符设为？
        dic = {"{": "}", "[": "]", "(": ")", "?": "?"}
        # 对栈（列表表示）初始化
        stack = ["?"]
        for c in s:
            # 左括号则入栈
            if c in dic:
                stack.append(c)

            elif dic[stack.pop()] != c:
                return False

        return len(stack) == 1