import random
# СДЕЛАЛ ВСЁ С БИБЛИОТЕКОЙ РАНДОМА, ВРОДЕ НЕ СЛОЖНО
def chislo(num_1, num_2):
    spis = [num_1, num_2]
    one = random.randint(num_1, num_2)
    two = random.randint(num_1, num_2)
    spis.append(one)
    spis.append(two)
    spis.sort()
    return spis

diapozon_1 = input('Введите два числа через пробел').split()

new = list(map(int, diapozon_1)) #ПОЛУЧАЛ ЧИСЛА КАК СТРОКУ, ПРЕОБРАЗОВЫВАЛ В СПИСОК, НИЖЕ ПОСТАВИЛ БЛОК ОБРАБОТКИ ТАК СКАЗАТЬ ОШИБОК ПОЛЬЗОВАТЕЛЯ
if len(new)>2:
    print('Нужно два числа')
elif new[0] == new[1]:
    print('Это одинаковые числа')
else:
    print(chislo(new[0],new[1]))


# print(chislo(13, 22))
# print(chislo(388, 389))
# print(chislo(1, 42))
# print(chislo(21, 244))