# -*- coding:utf-8 -*-
# -*- coding:utf-8 -*-
def find_num(n):
    if n < 1:
        return 0
    # 丑数：质因数只包含2\3\5中的一个或者多个
    # 丑数列表初始化
    num_list = [1]

    t2 = t3 = t5 = 0
    """
    ti 的定义：
    1.对任意的 t < ti, i * num_list[t] <= num_list[-1]
    2.对任意的 t > ti，i * num_list[t] > num_list[-1]
    """
    while len(num_list) < n:
        num_list.append(min(num_list[t2] * 2, num_list[t3] * 3, num_list[t5] * 5))

        # 重新查找 t2、t3、t5
        while 2 * num_list[t2] <= num_list[-1]:
            t2 += 1

        while 3 * num_list[t3] <= num_list[-1]:
            t3 += 1

        while 5 * num_list[t5] <= num_list[-1]:
            t5 += 1

    return num_list[-1]

# n = int(input())
print(find_num(10))