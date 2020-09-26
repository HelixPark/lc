
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'
        elif num1 == '1':
            return num2
        elif num2 == '1':
            return num1

        res = [0] * (len(num1) + len(num2))
        for i in range(len(num1)-1,-1,-1):
            for j in range(len(num2)-1,-1,-1):
                tmp = (ord(num1[i]) - ord('0')) * (ord(num2[j]) - ord('0'))
                tmp += res[i+j+1]
                res[i+j] += tmp // 10
                res[i+j+1] = tmp % 10

        res = [str(x) for x in res]
        # 把结尾未用到的0去除
        return ''.join(res).lstrip('0')