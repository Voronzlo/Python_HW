from random import randint

def input_data():
    a = -1
    while a < 0 or a > 1000:
        try: a = int(input('Введите a от 0 до 1000 => '))
        except: print('Введите число')
    return a

d = randint(0,1000)
flag = 'проиграл'
step = 10
print(f'Число от 0 до 1000 загадано. Ходите\n')
while step != 0 :
    a = int(input('Введите a от 0 до 1000 => '))
    if a > d:
        print(f'Меньше')
        step -= 1
    elif a < d:
        print(f'Больше')
        step -= 1
    elif a == d:
        flag = 'угадал'
        break
if step == 0:
    print(f'Ходы закончились ты {flag}')
else: print(f'ты {flag}')