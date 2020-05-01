def convert_temp(scale=None, source_temp=None):
    if scale == "F":
        return 'C', (source_temp - 32) * (5/9)
    elif scale == "f":
        return 'C', (source_temp - 32) * (5/9)
   
    elif scale == "C":
        return 'F', (source_temp * (9/5)) + 32
    elif scale == "c":
        return 'F', (source_temp * (9/5)) + 32
   
    else:
        print("Должно быть (F) или (C)!")

scale = input("Выберите Фаренгейт(F) или Цельсий(C): " )
source_temp = int(input("Введите температуру: " ))
s, m = convert_temp(scale, source_temp)
print(source_temp, "Градус", scale, "это", m, "Градус", s)
