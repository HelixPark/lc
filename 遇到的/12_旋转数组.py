# data为n*n数组:逆时针旋转90度
def fun(data):
    for row_index, row in enumerate(data):
        for col_index in range(row_index, len(row)):
            tmp = data[col_index][row_index]
            data[col_index][row_index] = row[col_index]
            data[row_index][col_index] = tmp
    return data

data = [[col for col in range(4)] for row in range(4)]
print(data)
print(fun(data))