# 41. Напишите программу вычисления арифметического выражения заданного строкой. Используйте операции +,-,/,*. приоритет операций стандартный.

# *Пример:* 

# 2+2 => 4; 
# 1+2*3 => 7; 
# 1-2*3 => -5;

# Добавьте возможность использования скобок, меняющих приоритет операций.

#    *Пример:* 

# 1+2*3 => 7; 
# (1+2)*3 => 9;


import sys



def is_digit(char:str):
    return True if char.isdigit() else False

text = "10/2*5"

dict_op = {'+': lambda x, y: x + y,
           '-': lambda x, y: x - y,
           '*': lambda x, y: x * y,
           '/': lambda x, y: x / y,
           }

list_dig =[]
list_operator = []
x=''
znak = 1

for i in range(len(text)):
    if text[i] == '-' and i==0:
        znak = -1
        continue
    if text[i].isalpha(): sys.exit("Неправильный ввод: нужны числа")
    if text[i].isdigit() : x += text[i]
    if text[i].isdigit() and  i == len(text)-1:
        list_dig.append(int(x))
    if not text[i].isdigit():
        list_operator.append(text[i])
        list_dig.append(int(x))
        x=''

if len(list_operator)>=len(list_dig):
    sys.exit("Недостаточно числовых данных")

list_dig[0] = list_dig[0]*znak
while '*' in list_operator or '/' in list_operator:
    for i in range(len(list_operator)):
        if list_operator[i]=='*' or list_operator[i]=='/':
            temp_res = (dict_op[list_operator[i]])(list_dig[i], list_dig[i+1])
            list_dig.pop(i)
            list_dig.pop(i)
            list_operator.pop(i)
            list_dig.insert(i, temp_res)
            break

while len(list_operator)!=0:

    temp_res = (dict_op[list_operator[0]])(list_dig[0],list_dig[1])
    list_operator.pop(0)
    list_dig.pop(0)
    list_dig.pop(0)
    list_dig.insert(0,temp_res)

print(f'{text} => {list_dig[0]}')