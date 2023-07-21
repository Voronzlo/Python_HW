if __name__ == '__main__':
    i = int(input("Введите число "))


    h = (format(i, '#x'))
    print(h) 
print(hex(i))
if hex(i) == h:
    print("Верно")
else:
    ("Не верно")