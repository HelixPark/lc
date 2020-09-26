
# utf-8
# utf-8
n, m = 2, 3
data = [[0] * m for _ in range(n)]
start = 1
for i in range(n):
    for j in range(m):
        data[i][j] = start
        start += 1
print(data)

# 矩阵转置：一行一行往里添加
def trans1(data):
    res = [[] for _ in data[0]]
    for row in data:
        for j in range(len(row)):
            res[j].append(row[j])
    return res

def trans2(data):
    data = zip(*data)
    data = [list(i) for i in data]
    return data


dataT = trans2(data)

print(dataT)
# 矩阵叉乘
def chafun(data,data2):
    res = [[0] * n for _ in range(n)]
    for i in range(n):
        row = data[i]
        for j in range(n):
            tmp = 0
            for k in range(len(row)):
                tmp += row[k] * data2[k][j]
            res[i][j] = tmp
    return res

print(chafun(data,dataT))
