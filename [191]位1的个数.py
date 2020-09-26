
class Solution:
    def hammingWeight(self, n: int) -> int:
        # 与运算：可以用来计算汉明权重

        # 二进制中，数字n中最低位的1总对应着n-1中的0，
        # 因此将n和n-1与运算总是能把n中最低位的1变成0,消掉，并保持其他位不变

        # ps:判断是不是2的指数（2的指数的数的二进制表示一定只有一个1）

        count = 0
        while n != 0:
            n = n & (n - 1)
            count += 1
        return count

