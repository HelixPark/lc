# -*- coding:utf-8 -*-
# -*- coding:utf-8 -*-

# formula = input()

formula = '3+8*2-6/4'

num01 = ''
num_list = []
symbol = []
count = 0

for i in formula:
    if i.isdigit():
        num01 += i
        count = 0
    elif i == '*' or i == '/' or i == '+' or i == '-':
        num_list.append(float(num01))
        num01 = ''
        symbol.append(i)
        count += 1
num_list.append(float(num01))

while symbol:
    while '*' in symbol or '/' in symbol:
        for i in symbol:
            if i == '*':
                j = symbol.index('*')
                result = num_list[j] * num_list[j+1]
                del num_list[j:j+2]
                num_list.insert(j,result)
                symbol.remove('*')
                break
            if i == '/':
                j = symbol.index('/')
                result = num_list[j] // num_list[j+1]
                del num_list[j:j+2]
                num_list.insert(j,result)
                symbol.remove('/')
                break
    while '+' in symbol or '-' in symbol:
        for i in symbol:
            if i == '+':
                j = symbol.index('+')
                result = num_list[j] + num_list[j+1]
                del num_list[j:j+2]
                num_list.insert(j,result)
                symbol.remove('+')
                break
            if i == '-':
                j = symbol.index('-')
                result = num_list[j] - num_list[j+1]
                del num_list[j:j+2]
                num_list.insert(j,result)
                symbol.remove('-')
                break
print(int(num_list[0]))